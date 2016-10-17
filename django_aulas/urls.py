from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import patterns, include, url

#-*-coding:utf-8 -*-
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_aulas.views.home', name='home'),
    # url(r'^django_aulas/', include('django_aulas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^aula3/$', 'aula3.views.index', name='aula3_index'),
    url(r'^aula3/(?P<id>\d+)/$', 'aula3.views.detail', name='aula3_detail'),
    url(r'^fatorial/$', 'aula3.views.fatorial', name='calculo_fatorial'),
    url(r'^aula4/$', 'aula4.views.index', name='aula4_index'),
    url(r'^teste/$', 'aula4.views.teste', name='aula4_teste'),
    url(r'^metodo/$', 'aula3.views.getMetodo', name='aula3_getMetodo')
)

if settings.DEBUG:
    urlpatterns += patterns('',
                    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                    )

urlpatterns += staticfiles_urlpatterns()