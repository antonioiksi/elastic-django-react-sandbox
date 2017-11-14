import json

from django.contrib.auth.models import User

from app_data_bins.models import Bin, BinItem
from django.test import TestCase

data1 = """
{
    "data": {
        "field1": 1
    }
}
"""
data2 = """
{
    "data": {
        "field2": 2
    }
}
"""

class DataBinsModelsTest(TestCase):
    """ Test module for Log model """

    def setUp(self):
        user = User.objects.get(username='antonio')
        bin = Bin.objects.create( user=user, name='bin')
        binItem1 = BinItem.objects.create( bin=bin, data=json.loads(data1))
        binItem2 = BinItem.objects.create(bin=bin, data=json.loads(data2))


    def test_bin(self):

        bin = Bin.objects.get(name='bin')
        binItems = BinItem.objects.filter(bin=bin)

        self.assertEqual(1, 1)