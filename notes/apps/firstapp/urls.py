from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^login$', views.login),
    url(r'^notes$', views.notes),
    url(r'^notes/add$', views.addnote),
]

