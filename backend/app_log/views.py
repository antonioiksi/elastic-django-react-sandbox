import datetime
import json

from django.shortcuts import render

from .mixins import RequestLogViewMixin
from .models import Log
from .serializers import LogSerializer
from rest_framework import generics



class LogViewSet(RequestLogViewMixin, generics.ListAPIView):
    serializer_class = LogSerializer


    def get_queryset(self):
        user = self.request.user

        return Log.objects.all()





