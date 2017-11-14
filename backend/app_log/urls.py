from django.conf.urls import url, include
from rest_framework import routers

from .views import LogListView, LogListAuthView

#router = routers.DefaultRouter()
#router.register(r'logs', LogViewSet)


urlpatterns = [
    url(r'^all/$', LogListView.as_view(), name='log_List'),
    url(r'^all-auth/$', LogListAuthView.as_view(), name='log_List_auth'),
]