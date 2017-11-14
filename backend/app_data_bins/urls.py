from django.conf.urls import url


from app_data_bins.views.view_bin import BinListView, BinDeleteView, BinCreateView
from app_data_bins.views.view_bin_item import BinItemsView

app_name = 'data_bins'
urlpatterns = [

    url(r'^list/$', BinListView.as_view(), name='bin-list'),
    url(r'^delete/(?P<bin_pk>.+)$', BinDeleteView.as_view(), name='bin-delete'),
    url(r'^create/$', BinCreateView.as_view(), name='bin-create'),

    url(r'^items/list/(?P<bin_pk>.+)$', BinItemsView.as_view(), name='items-list'),
    url(r'^items/create/(?P<bin_pk>.+)$', BinItemsView.as_view(), name='items-create'),
    url(r'^items/delete/(?P<item_pk>.+)$', BinItemsView.as_view(), name='items-delete'),
    url(r'^items/update/(?P<item_pk>.+)$', BinItemsView.as_view(), name='items-update'),

]


