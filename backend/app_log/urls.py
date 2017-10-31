from django.conf.urls import url, include
from rest_framework import routers

from .views import LogViewSet

#router = routers.DefaultRouter()
#router.register(r'logs', LogViewSet)


urlpatterns = [
    url(r'^all/$', LogViewSet.as_view()),
]