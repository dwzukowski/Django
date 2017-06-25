from django.conf.urls import url
#from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^books$', views.books),
    url(r'^logout$', views.logout),
    url(r'^books/addbook$', views.addbook),
    url(r'^books/addreview$', views.addreview),
    url(r'^books/addbook/(?P<book_id>\d+)$', views.showreviews),
]

