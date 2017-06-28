from django.conf.urls import url
from . import views

urlpatterns= [
    urls(r'^$', views.toindex, name='toindex')
]