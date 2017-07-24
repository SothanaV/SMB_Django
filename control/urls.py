from django.conf.urls import url
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^data/(?P<nodeid>\d+)/(?P<temp>\d+\.\d+)/(?P<humi>\d+\.\d+)/(?P<key>\d+)/$', views.getdata, name='getdata'),
]