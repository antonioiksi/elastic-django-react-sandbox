import json
import os
import requests
import pprint
import copy
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import generics, views, status

from app_log.mixins import RequestLogViewMixin

from backend import settings
from .permissions import PublicEndpoint
from .models import Attribute
from .serializers import AttributeSerializer

#def
#ES_QUERY_TEMPLATE =


class AttributeListView(RequestLogViewMixin, generics.ListAPIView):
    """

    Возвращаем список разрешенных атрубутов для поиска

    """
    permission_classes = (PublicEndpoint,)
    serializer_class = AttributeSerializer
    queryset = Attribute.objects.all()


class MultifieldSearchMatchView(RequestLogViewMixin, views.APIView):
    # TODO добавить возможность нормального чтения документации
    """
{
  'query': {
    'bool': {
      'should': [
        {
          'match': {
            'value': '4352435342532'
          }
        },
        {
          'match': {
            'name': 'phone'
          }
        }
      ]
    }
  }
}

    """
    permission_classes = (PublicEndpoint,)
    def post(self, request, *args, **kwargs):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(dir_path, 'es-query-templates.json')) as json_queries:
            d = json.load(json_queries)
            #print(d)
        query = d['MultifieldSearchMatch']

        #val1 = {'play_name':'Henry', 'speaker':'king' }
        #val2 = {'f2': 'fv3'}
        #vals= [val1]
        vals = request.data
        pprint.pprint(vals)

        lstR = []
        for val in vals:
            for k, v in val.items():
                match = {'match':{k:v}}
                #json_match_val1 = copy.deepcopy(json_match)
                #json_match_val1['match'][k]=v
                query['query']['bool']['should'].append(match)
            pprint.pprint(query)
            r = requests.post(settings.ELASTIC_SEARCH_URL + "_search", json.dumps(query))

            if r.status_code!=200:
                return Response('app_elastic error for query '+json.dumps(query), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            lstR.append(r.json())

        return Response( lstR, status=status.HTTP_200_OK)
        #return Response( d, status=status.HTTP_200_OK)s


class ElasticProxyView(RequestLogViewMixin, views.APIView):
    """

    Transport query to ElasticSearch and get the answer

    """
    def post(self, request, *args, **kwargs):
        r = requests.post(settings.ELASTIC_SEARCH_URL+"_search", json.dumps(request.data))
        if r.status_code == 200:
            return Response( r.json(), status=status.HTTP_200_OK)
        else:
            return Response('app_elastic error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
