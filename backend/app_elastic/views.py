import base64
import json

import requests
import zlib
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers, views, status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from rest_framework.decorators import authentication_classes, permission_classes, api_view


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def hello_world(request):
    print(request.user)
    return Response([{"message":"Hello world!"},{"message":"Hello world!"}])

#class QuerySerializer(serializers.Serializer):
    #query = serializers.CharField()

class ElasticView(views.APIView):
    def post(self, request, *args, **kwargs):
        #serializer = QuerySerializer(data=request.data)
        #serializer.is_valid()
        #js = serializer.validated_data


        r = requests.post("http://127.0.0.1:9200/_search", json.dumps(request.data))
        if r.status_code == 200:
            return Response(
                r.json(), status=status.HTTP_200_OK)
        else:
            return Response('app_elastic error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        #raise APIException("There was a problem!")


class DecodeIndexView(views.APIView):
    def get(self):
        user = self.request.user
        indexname = self.kwargs['indexname']
        try:
            decoded = zlib.decompress(base64.b32decode(indexname, True), 40).decode()
            return Response( decoded, status=status.HTTP_200_OK)
        except Exception as e:
            return Response('"errorMessage":%s' % e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

