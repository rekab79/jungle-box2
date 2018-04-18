
from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from jungle import views
from django.urls import include, path

urlpatterns = [
    
    
    path('admin/', admin.site.urls),
    path('jungle/',include('jungle.urls'),name='index'),
    #path('jungle/register',include('jungle.urls'),name=register),
    ]
