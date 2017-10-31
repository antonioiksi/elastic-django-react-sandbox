from django.conf.urls import url

from .views import ElasticView, DecodeIndexView
from . import views

urlpatterns = [
    url(r'^search/$', ElasticView.as_view()),
    url(r'^decodeindex/(?P<indexname>.+)$', DecodeIndexView.as_view()),
    url(r'^hello_world/$',
        views.hello_world,
        name='hello_world'),

]