import datetime
import json

from django.shortcuts import render
from django.urls import reverse, resolve

from .mixins import RequestLogViewMixin
from .models import Log
from .serializers import LogSerializer
from rest_framework import generics, versioning


class LogViewSet(RequestLogViewMixin, generics.ListAPIView):
    serializer_class = LogSerializer


    def get_queryset(self):
        #print(self.request.META['HTTP_REFERER'])
        #print(self.request.path)
        #print(self.request.version)
        #print(self.request.path_info)

        user = self.request.user

        r = resolve(self.request.path_info)
        print(r.namespace)

        return Log.objects.all()

        #return Log.objects.all()





