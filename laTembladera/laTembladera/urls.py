from django.conf.urls import patterns, include, url
from laTembladera import settings
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
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^index/$', index),

    #EMPRESA
    url(r'^origen/$', origen),
    url(r'^misionYvision/$',misionYvision),
    url(r'^objetivos/$',objetivos),
    url(r'^politicas/$',politicas),
    url(r'^estructuraFuncional/$',estructuraFuncional),



    url(r'^productos/$',productos),
    url(r'^proyectos/$',proyectos),
    url(r'^galeria/$',galeria),
    url(r'^florayfauna/$',florayfauna),



    #NOTICIAS
    url(r'^ver_noticia/^', verNoticia),
    url(r'^ver_noticia/(?P<id_noticia>.*)/$',ver_noticia,name="ver_noticia"),
    url(r'^noticias/$', noticias), #ver todas las noticias

)
