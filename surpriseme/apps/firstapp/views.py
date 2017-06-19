# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random

def index(request):
    return render(request, 'firstapp/index.html')

def results(request):
    return render(request, 'firstapp/results.html')

def process(request):
    values= ['oranges', 'mysterious','sick', 'smooth', 'stare', 'nauseating', 'loss', 'horrible', 'argument', 'hover', 'crib', 'wacky']
    count= int(request.POST['number'])
    request.session['result']= []
    while count > 0:
        request.session['result'].append(random.choice(values))
        print request.session['result']
        count-=1
    return redirect('/results')
