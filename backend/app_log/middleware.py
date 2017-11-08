import json
import socket
import time

import datetime
from app_log.models import Log
from django.contrib.auth.models import User


class RequestLogMiddleware(object):
    def process_request(self, request):
        print('process_request from RequestLogMiddleware')
        request.start_time = time.time()

        if request.user.pk != None:
            try:
                user_id = int(request.user.pk)
                user = User.objects.get(id=user_id)
            except  User.DoesNotExist:
                print(user_id)
        else:
            user = None

        if request.method=='POST':
            try:
                query = json.loads(request.body.decode("utf-8"))
                #query = json.dumps( request.body.decode("utf-8"))
                #query = json.dumps(request.body)
            except Exception as err:
                print('Error json {0}'.format(err))
                query = None
        else:
            query = None

        log = Log(user=user,
                    ip=request.META['REMOTE_ADDR'],
                    datetime=datetime.datetime.now(),
                    query=query,
                    method=request.method,
                    event=request.path_info)
        log.save()


    def process_response(self, request, response):
        print('process_response from RequestLogMiddleware')

        if response['content-type'] == 'application/json':
            if getattr(response, 'streaming', False):
                response_body = '<<<Streaming>>>'
            else:
                response_body = response.content
        else:
            response_body = '<<<Not JSON>>>'

        log_data = {
            'user': request.user.pk,

            'remote_address': request.META['REMOTE_ADDR'],
            'server_hostname': socket.gethostname(),

            'request_method': request.method,
            'request_path': request.get_full_path(),
            #'request_body': request.body,

            'response_status': response.status_code,
            'response_body': response_body,

            'run_time': time.time() - request.start_time,
        }

        #print(request.user.pk)

        # save log_data in some way
        #print(log_data)


        return response