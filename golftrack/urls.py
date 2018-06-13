from django.conf.urls import include, url
from django.contrib import admin
from database1 import views

urlpatterns = [
    url(r'^database1/', include('database1.urls')),
    url(r'^$', views.home),
]