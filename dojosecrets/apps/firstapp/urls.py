from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),  
    url(r'^login$', views.login),
    url(r'^secrets$', views.secrets), 
    url(r'^logout$', views.logout), 
    url(r'^postsecret$', views.postsecret),
    url(r'^likesecret/(?P<secretid>\d+)$', views.likesecret),
    url(r'^deletesecret/(?P<secretid>\d+)$', views.deletesecret),
]

