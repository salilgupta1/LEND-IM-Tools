from django.conf.urls import patterns, include, url
from django.contrib import admin
from tools import views
admin.autodiscover()

urlpatterns = patterns('',

    #/clients app
  	url(r'^clients/',include('clients.urls',namespace = 'clients')),

    #/admin pages
    url(r'^admin/', include(admin.site.urls)),

    #login urls
    url(r'^$',views.home_login,name= 'home_login'),

    url(r'^logout/',views.logOut,name = 'logOut'),
    
    #registration urls
    url(r'^register_user/$',views.register_user,name = 'register_user'),

    url(r'^register_user_success/(?P<username>\w+)/$',views.register_user_success, name = 'register_user_success'),
)




