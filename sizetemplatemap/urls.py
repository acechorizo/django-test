from django.conf.urls import patterns, url

from sizetemplatemap import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<creative_size_id>\d+)/$', views.detail, name='detail'),
)
