from django.conf.urls import patterns, url

from clients import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^loan/$',views.client, {"clientType": "LOAN"},name = 'loan'),
    url(r'^btp/$',views.client, {"clientType": "BTP"},name = 'btp'),
    url(r'^edit_client/(?P<client_UUID>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$',views.edit_client,name = 'edit_client'),
    url(r'^create_client/$',views.create_client, name = 'create_client'),
    url(r'^delete_client/$',views.delete_client,name = 'delete_client'),
    url(r'^ajax_coordinates/$',views.ajax_coordinates,name='ajax_coordinates')

)
#clients/
#clients/loan/
#clients/btp/
#clients/edit_client/client_uuid/
#clients/create_client/
#clients/delete_client/