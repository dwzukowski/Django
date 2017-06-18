# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    print request.method    
    return render(request,'firstapp/index.html')
def testimonials(request):
    print request.method
    return render(request,'firstapp/testimonials.html')

