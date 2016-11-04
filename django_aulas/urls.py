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
    url(r'^metodo/$', 'aula3.views.getMetodo', name='aula3_getMetodo'),
    url(r'^aula6/$', 'aula6.views.index', name='aula6_index'),
    url(r'^aula6/(?P<id>\d+)/$', 'aula6.views.detail', name='aula6_detail'),
    url(r'^aula7/$', 'aula7.views.index', name='aula7_index'),
    url(r'^aula7/sair/$', 'aula7.views.sair', name='aula7_sair'),
    url(r'^aula7/view_protegida/$', 'aula7.views.view_protegida', name='aula7_view_protegida'),
    url(r'^aula7/view_protegida2/$', 'aula7.views.view_protegida2', name='aula7_view_protegida2')

)

if settings.DEBUG:
    urlpatterns += patterns('',
                    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                    )

urlpatterns += staticfiles_urlpatterns()