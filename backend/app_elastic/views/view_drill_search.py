import json
from pprint import pprint

import requests
from rest_framework import views, status
from rest_framework.response import Response

from backend.permissions import PublicEndpoint
from backend import settings
from app_log.mixins import RequestLogViewMixin

input_json = """
{

    "deep": "3",
    "style": "strong",
    [
        {
            "phone": "2345233425",
            "name": "name 1"
        },
        {
            "type": "234534534",
        }
    ]
}"""

input_query = """{'query': {'bool': {'should': [{'match': {'speaker': 'king'}},
                               {'match': {'play_name': 'Henry'}}]}}}"""


query_match_all = """
{
    "query": {
        "match_all": {}
    }
}"""

class DrillSearch(RequestLogViewMixin, views.APIView):
    """

    """
    permission_classes = (PublicEndpoint,)

    def post(self, request, *args, **kwargs):
        # TODO add checking input param http://json-schema.org/

        try:
            es_search = requests.post(settings.ELASTIC_SEARCH_URL + "/_search", json.dumps(request.data))
            #es_search = requests.get(settings.ELASTIC_SEARCH_URL + "/_search")
            search = es_search.json()
            # output_dict = [x for x in data if x['type'] == '1']
            #values_arr = [x['_source']['play_name'] for x in data['hits']['hits']]
            #pprint(values_arr)
        except Exception as e:
            return Response('app_elastic error: %s' % e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


        mappings_res = {}

        hits_arr = search['hits']['hits']
        for hit in hits_arr:
            index_name = hit['_index']
            if index_name not in mappings_res:

                try:
                    es_mapping = requests.get(settings.ELASTIC_SEARCH_URL + '/' + index_name + '/_mapping')
                    mapping = es_mapping.json()
                except Exception as e:
                    return Response('app_elastic error getting mapping: %s' % e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                mapping = mapping[index_name]['mappings']

                tables_res={}
                for table_name in mapping:
                    table_mapping = mapping[table_name]
                    #d = mapping[index_name]['mappings']['act']['properties']
                    #tables_mapping = [mapping[key] for key in mapping]
                    temp_dict = table_mapping['properties']
                    field_arr = [temp_dict[key] for key in temp_dict if temp_dict[key].get('fields') is not None]

                    tables_res[table_name] = field_arr

                mappings_res[index_name] = tables_res
                # TODO проход по JSON элементам а не по массиву
                # [d[key] for key in d if d[key]['type']=='text']
                # d = mapping['shakespeare']['mappings']['act']['properties']
                # [d[key] for key in d if d[key].get('fields') is None]

            #es_mapping = requests.get(settings.ELASTIC_SEARCH_URL + "shakespeare?pretty")
            #mapping = es_mapping.json()

        result = {}
        #source_arr = [x['_source'] for x in search['hits']['hits']]
        result['data'] = search['hits']['hits']
        result['mapping'] = mappings_res

        return Response(result, status=status.HTTP_200_OK)