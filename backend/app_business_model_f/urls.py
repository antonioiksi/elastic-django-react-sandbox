from django.conf.urls import url

from .views import AttributeListView, ElasticProxyView, MultifieldSearchMatchView

urlpatterns = [
    url(r'^attributes/$', AttributeListView.as_view()),
    url(r'^elasticproxy/$', ElasticProxyView.as_view()),
    url(r'^multifield-search-match/$', MultifieldSearchMatchView.as_view()),

]