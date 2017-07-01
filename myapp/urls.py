from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^$', views.control, name='control'),
    url(r'^$', views.smb, name='smb'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^signout/', views.signout, name='signout'),
    url(r'^change_password/', views.change_password, name='change_password'),

    url(r'^(?P<nodeid>\d+)/$', views.getdata, name='getdata'),
]