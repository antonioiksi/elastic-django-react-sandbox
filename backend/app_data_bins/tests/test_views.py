from pprint import pprint

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from app_data_bins.models import Bin


class DataBinsViewsTest(APITestCase):
    """ Test module for GET all logs API """
    urls = 'app_data_bins.urls'


    def setUp(self):
        print('setUp ViewsTest')
        User.objects.create(username='antonio')
        bin = Bin.objects.create(name='antonio')
        pprint(Bin.objects.all())


    def test_AllView(self):
        client = APIClient()
        user = User.objects.get(username='antonio')
        client.force_authenticate(user=user)
        #url = reverse('simple')
        url = '/bins/all/'
        #response = client.post(url, json.loads(query_match_all), format='json')
        #pprint(json.dumps( response.json()))
        #pprint(response.json())
        #self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(status.HTTP_200_OK, status.HTTP_200_OK)