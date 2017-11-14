import json

import requests
from rest_framework import views, status
from rest_framework.response import Response

from backend import settings
from app_log.mixins import RequestLogViewMixin


class DeepDrillSearch(RequestLogViewMixin, views.APIView):
    """
    post:
    Tranport json to ES and get response
    """
    def post(self, request, *args, **kwargs):
        #serializer = QuerySerializer(data=request.data)
        #serializer.is_valid()
        #js = serializer.validated_data


        r = requests.post(settings.ELASTIC_SEARCH_URL+"/_search", json.dumps(request.data))
        if r.status_code == 200:
            return Response( r.json(), status=status.HTTP_200_OK)
        else:
            return Response('app_elastic error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #raise APIException("There was a problem!")
