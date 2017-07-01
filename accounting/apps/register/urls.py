from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^logout$', views.logout),
    url(r'^login$', views.login),
    url(r'^company$', views.company),
    url(r'^company/newconcern$', views.newconcern),
    url(r'^company/financials/(?P<concern_id>\d+)$', views.financials),
    url(r'^company/financials/getstarted/(?P<concern_id>\d+)$', views.getstarted),
    url(r'^addAssetType$', views.addAssetType),
    url(r'^company/addAsset$', views.addAsset),   
    url(r'^destroy/(?P<asset_id>\d+)$', views.destroyAsset),
    url(r'^destroy/confirm/(?P<asset_id>\d+)$', views.confirmDestroyAsset),
    url(r'^createLiabilityType$', views.createLiabilityType),
    url(r'^company/addLiability$', views.addLiability),
    url(r'^destroy/liability/(?P<liability_id>\d+)$', views.destroyLiability),
    url(r'^destroy/liability/confirm/(?P<liability_id>\d+)$', views.confirmDestroyLiability),
]

