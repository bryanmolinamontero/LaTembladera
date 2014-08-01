from django.conf.urls import patterns, include, url
from tembladera.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'laTembladera.views.home', name='home'),
    # url(r'^laTembladera/', include('laTembladera.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', index),
     url(r'^origen/$', origen),
)
