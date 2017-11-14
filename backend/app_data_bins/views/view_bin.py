import json

from django.core import serializers
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, views, status
from rest_framework.response import Response

from app_data_bins.models import Bin
from app_data_bins.serializers import BinSerializer
from backend.permissions import PublicEndpoint
from app_log.mixins import RequestLogViewMixin



class BinListView(RequestLogViewMixin, generics.ListAPIView):
    """Get all logs without authorization"""
    permission_classes = (PublicEndpoint,)
    serializer_class = BinSerializer

    def get_queryset(self):
        user = self.request.user
        return Bin.objects.filter(user=user)


class BinDeleteView(RequestLogViewMixin, views.APIView):
    #permission_classes = (PublicEndpoint,)
    def get(self, request, bin_pk):
        try:
            Bin.objects.get(pk=bin_pk).delete()
            return Response("", status=status.HTTP_200_OK)
        except Exception as e:
            return Response('data_bins error deleting: %s' % e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class BinCreateView(RequestLogViewMixin, views.APIView):
    #permission_classes = (PublicEndpoint,)
    def post(self, request, *args, **kwargs):
        user = self.request.user
        bin = json.dumps(request.data)
        try:
            bin = Bin.objects.create(user=user, name=bin['name'])
            return Response("", status=status.HTTP_200_OK)
        except Exception as e:
            return Response('data_bins error creating: %s' % e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)