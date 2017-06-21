from django.conf.urls import url
from . import views
#from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add_course),
    url(r'^destroy/(?P<id>\d+)$', views.destroy), 
    url(r'^confirm_delete/(?P<id>\d+)$', views.confirm_destroy),   
]
