# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'firstapp/index.html')
def ninjas(request):
    return render(request, 'firstapp/ninjas.html')
def show(request, color):
    print "Show OK"
    if color== 'red' or color== 'blue' or color== 'purple' or color== 'orange':
        context={
            "color": color
        }
        return render(request, 'firstapp/show.html', context)
    else:
        context= {
            "color": 'april'
        }
        return render(request, 'firstapp/show.html', context)