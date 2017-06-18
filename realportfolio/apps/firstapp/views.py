# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request,'firstapp/index.html')
def testimonials(request):
    return render(request,'firstapp/testimonials.html')
def projects(request):
    return render(request,'firstapp/projects.html')
def about(request):
    return render(request,'firstapp/about.html')    

# Create your views here.
