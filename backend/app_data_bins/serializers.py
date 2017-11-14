from rest_framework import serializers

from .models import Bin, BinItem


class BinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bin
        fields = ('user','name',)

class BinItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BinItem
        fields = ('bin','query','data','mapping',)
