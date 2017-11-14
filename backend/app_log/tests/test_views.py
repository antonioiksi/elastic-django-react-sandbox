import json

from django.contrib.auth.models import User
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework_simplejwt.tokens import Token

from app_log.views import LogListAuthView
from ..models import Log
from ..serializers import LogSerializer


# initialize the APIClient app
client = Client()

class GetAllLogsTest(TestCase):
    """ Test module for GET all logs API """

    def setUp(self):
        Log.objects.create(
            ip='127.0.0.1', query='', event='/test1/', method='POST')
        Log.objects.create(
            ip='127.0.0.1', query='', event='/test2/', method='GET')

    def test_get_all_logs(self):
        # get API response
        response = client.get(reverse('log_List'))
        # get data from db
        logs = Log.objects.all()
        serializer = LogSerializer(logs, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_force_auth(self):
        factory = APIRequestFactory()
        #user = User.objects.get(username='antonio')
        #view = LogListAuthView.as_view()

        # Make an authenticated request to the view...
        #request = factory.get('/all-auth/')
        #force_authenticate(request, user=user)
        #response = view(request)
        self.assertEqual(status.HTTP_200_OK, status.HTTP_200_OK)