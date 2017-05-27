from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.control, name='control'),
    url(r'^$', views.smb, name='smb'),

]