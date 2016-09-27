from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<location_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^temperatures/$', views.temperatures, name='temperatures'), 
#    url(r'^(?P<location_id>[0-9]+)/routes/$', views.routes, name='routes'), 
    url(r'^routes/$', views.routes, name='routes'), 
]
