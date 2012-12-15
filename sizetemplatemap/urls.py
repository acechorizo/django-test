from django.conf.urls import patterns, url

from sizetemplatemap import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index\.html', views.index, name='index'),
    url(r'^(?P<creative_size_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<creative_size_id>\d+)/edit/$', views.cs_edit, name='edit'),
)
