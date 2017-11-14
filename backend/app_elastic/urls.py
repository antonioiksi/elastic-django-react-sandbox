from django.conf.urls import url

from app_elastic.views import views
from app_elastic.views.view_deep_drill_search import DeepDrillSearch
from app_elastic.views.view_drill_search import DrillSearch
from app_elastic.views.view_simple_search import SimpleSearch
from app_elastic.views.view_decode_index import DecodeIndexView

urlpatterns = [

    url(r'^search/simple/$', SimpleSearch.as_view(), name='simple'),
    url(r'^search/drill/$', DrillSearch.as_view(), name='drill'),
    url(r'^search/deep-drill/$', DeepDrillSearch.as_view(), name='deep-drill'),


    url(r'^decodeindex/(?P<indexname>.+)$', DecodeIndexView.as_view()),

    url(r'^test_auth_free/$', views.test_auth_free, name='test_auth_free'),


]


