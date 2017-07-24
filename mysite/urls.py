"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home,name='home'),
    url(r'^control/', views.control, name='control'),
    url(r'^smb/', views.smb, name='smb'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^signout/', views.signout, name='signout'),
    url(r'^change_password/', views.change_password, name='change_password'),
    #url(r'^data/(?P<nodeid>\d+)/(?P<temp>\d+\.\d+)/(?P<humi>\d+\.\d+)/(?P<key>\d+)/$', views.getdata, name='getdata'),
    #url(r'^addprogram/', views.addprofile, name='addprogram'),
    #url(r'data/', include('getdata.urls')),
    url(r'^data/', include('AppControl.urls')),
    #url(r'^getprogram/', views.getprogram, name='getprogram'),




]
