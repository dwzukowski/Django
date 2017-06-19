from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    # -? runs even if user enters negative number
    url(r'^-?(?P<number>\d+)$', views.process),    

]
