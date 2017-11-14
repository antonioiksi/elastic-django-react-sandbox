import json

from django.core import serializers
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, views, status
from rest_framework.response import Response

from backend.permissions import PublicEndpoint
from app_log.mixins import RequestLogViewMixin

from app_data_bins.models import Bin, BinItem


class BinItemsView(RequestLogViewMixin, views.APIView):
    permission_classes = (PublicEndpoint,)

    def get(self, request, bin_pk):
        user = self.request.user
        #bin_pk = self.kwargs['bin_pk']
        bin = Bin.objects.get(pk=bin_pk)
        rows = BinItem.objects.filter(bin=bin)
        result = serializers.serialize('json', rows, fields=('id','data','bin'))
        result = serializers.serialize('json', rows)
        #result = bin.name
        return Response(result, status=status.HTTP_200_OK)


