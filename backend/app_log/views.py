import datetime
import json

from django.shortcuts import render
from django.urls import reverse, resolve

from backend.permissions import PublicEndpoint
from .mixins import RequestLogViewMixin
from .models import Log
from .serializers import LogSerializer
from rest_framework import generics, versioning


class LogListView(RequestLogViewMixin, generics.ListAPIView):
    """Get all logs without authorization"""
    serializer_class = LogSerializer
    permission_classes = (PublicEndpoint,)

    def get_queryset(self):
        user = self.request.user

        r = resolve(self.request.path_info)
        print(r.namespace)

        return Log.objects.all()

class LogListAuthView(RequestLogViewMixin, generics.ListAPIView):
    """Get all logs with authorization"""
    serializer_class = LogSerializer
    def get_queryset(self):
        user = self.request.user

        r = resolve(self.request.path_info)
        print(r.namespace)

        return Log.objects.all()




