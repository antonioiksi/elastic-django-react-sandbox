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

from django.views import generic
from rest_framework.schemas import get_schema_view
from rest_framework_simplejwt.views import (
    TokenVerifyView)

from rest_framework.documentation import include_docs_urls
from django.conf.urls import include, url

from .views import TokenObtainPairWithLoggingView, TokenRefreshViewLoggingView, EchoView, CurrentUserView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # redirect
    url(r'^$', generic.RedirectView.as_view(url='/api/', permanent=False)),

    url(r'^api/$', get_schema_view()),
    url(r'^api/docs/', include_docs_urls(title='Api docs')),

    # JWT authentification
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/token/obtain/$', TokenObtainPairWithLoggingView.as_view()),
    url(r'^auth/token/refresh/$', TokenRefreshViewLoggingView.as_view()),
    url(r'^auth/token/verify/', TokenVerifyView.as_view()),

    # Main rest api
    url(r'^api/business/', include('app_business_model_f.urls', namespace='v1')),
    #
    url(r'^elastic/', include('app_elastic.urls', namespace='elastic')),

    url(r'^bins/', include('app_data_bins.urls', namespace='app_data_bins')),

    # Additional rest api
    url(r'^tools/user-info/$', CurrentUserView.as_view()),
    url(r'^tools/log/', include('app_log.urls')),
    # url(r'^api/v1/log/', include('app_log.urls', namespace='v1')),
    # url(r'^api/v2/log/', include('app_log.urls', namespace='v2')),


    # Testing rest api
    url(r'^test/echo/$', EchoView.as_view(), name='echo'),







]

