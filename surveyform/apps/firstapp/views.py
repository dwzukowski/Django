# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    try:
        request.session['count']
        return render(request,'firstapp/index.html')    
    except KeyError: 
        request.session['count']=0
        return render(request,'firstapp/index.html')
    #another way to resolve issue of undefined session variable --> 
    #if not 'count' in request.session:
        #request.session['count']=0
    #else:
        #request.session['count']+=1 

def results(request):
    if request.method == 'POST':
        request.session['name'] = request.POST['name'] 
        print request.session['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comments'] = request.POST['comments']
        request.session['count'] += 1
        return redirect('/show')
    else:
        return redirect('/')

def show(request):
    return render(request,'firstapp/show.html')