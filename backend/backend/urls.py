"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import resolve

from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


from rest_framework import views, serializers, status, versioning
from rest_framework.response import Response


from rest_framework.documentation import include_docs_urls
from django.conf.urls import include, url


class MessageSerializer(serializers.Serializer):
    message = serializers.CharField()

class EchoView(views.APIView):
    """
    post:
    load message via post method
    """
    def post(self, request, *args, **kwargs):

        r = resolve(self.request.path_info)

        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)



urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # redirect
    url(r'^$', generic.RedirectView.as_view(url='/api/', permanent=False)),

    url(r'^api/$', get_schema_view()),
    url(r'^api/docs/', include_docs_urls(title='Api docs')),

    # allow login and logout
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/token/obtain/$', TokenObtainPairView.as_view()),
    url(r'^auth/token/refresh/$', TokenRefreshView.as_view()),


    url(r'^test/echo/$', EchoView.as_view(), name='echo'),


    url(r'^api/business/', include('app_business_model_f.urls')),

    url(r'^api/elastic/', include('app_elastic.urls')),



    url(r'^api/log/', include('app_log.urls')),
    #url(r'^api/v1/log/', include('app_log.urls', namespace='v1')),
    #url(r'^api/v1/log/', include('app_log.urls', namespace='v2')),



]

