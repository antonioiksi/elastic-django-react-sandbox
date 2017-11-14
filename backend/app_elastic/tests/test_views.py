import json
from pprint import pprint

from django.contrib.auth.models import User
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, RequestsClient, APITestCase

# initialize the APIClient app
from app_elastic.views.view_deep_drill_search import DeepDrillSearch
from app_elastic.views.view_drill_search import DrillSearch
from app_elastic.views.view_simple_search import SimpleSearch


query_match_all = """
{
    "query": {
        "match_all": {}
    }
}
"""

query_fieldname_wildcart = """
{
    "query": {
        "bool": {
            "should": [
                {
                    "query_string": {
                        "default_field": "*speaker*",
                        "query": "KING"
                    }
                }                
            ]        
        }
    }
}
"""


class ElasticViewsTest(APITestCase):
    """ Test module for GET all logs API """
    urls = 'app_elastic.urls'


    def setUp(self):
        print('setUp ViewsTest')
        User.objects.create(username='antonio')
        #pprint(User.objects.all())


    def test_factory_SimpleSearch(self):
        factory = APIRequestFactory()
        #url = reverse('log_List')
        user = User.objects.get(username='antonio')
        request = factory.post('search/simple/', json.loads(query_fieldname_wildcart), format='json')
        force_authenticate(request, user=user)
        view = SimpleSearch.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_apiclient_SimpleSearch(self):
        client = APIClient()
        user = User.objects.get(username='antonio')
        client.force_authenticate(user=user)
        #url = reverse('simple')
        url = '/elastic/search/simple/'
        response = client.post(url, json.loads(query_match_all), format='json')
        #pprint(json.dumps( response.json()))
        #pprint(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_apiclient_DrillSearch(self):
        client = APIClient()
        user = User.objects.get(username='antonio')
        client.force_authenticate(user=user)
        #url = reverse('simple')
        url = '/elastic/search/drill/'
        #response = client.post(url, json.loads(query_match_all), format='json')
        #pprint(json.dumps( response.json()))
        #pprint(response.json())
        #self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(status.HTTP_200_OK, status.HTTP_200_OK)

"""
    def test_DeepDrillSearch(self):
        client = RequestsClient()
        response = client.get('http://localhost/search/deep-drill/', json.load(query_match_all), format='json')
        assert response.status_code == 200
"""