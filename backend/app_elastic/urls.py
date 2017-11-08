from django.conf.urls import url

from .views import ElasticView, DecodeIndexView
from . import views



urlpatterns = [

    url(r'^search/$', ElasticView.as_view()),

    url(r'^decodeindex/(?P<indexname>.+)$', DecodeIndexView.as_view()),

    url(r'^test_auth_free/$', views.test_auth_free, name='test_auth_free'),



]


