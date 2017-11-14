from django.test import TestCase
from ..models import Log


class LogTest(TestCase):
    """ Test module for Log model """

    def setUp(self):
        Log.objects.create(
            ip='127.0.0.1', query='', event='/test1/', method='POST')
        Log.objects.create(
            ip='127.0.0.1', query='', event='/test2/', method='GET')

    def test_log_event(self):
        log_test1 = Log.objects.get(event='/test1/')
        log_test2 = Log.objects.get(event='/test2/')
        self.assertEqual(
            log_test1.get_event(), "Log belongs to /test1/ events.")
        self.assertEqual(
            log_test2.get_event(), "Log belongs to /test2/ events.")