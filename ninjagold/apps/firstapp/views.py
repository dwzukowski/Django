# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random

def index(request):
    try:
        request.session['bank']
        request.session['activities']
        return render(request,'firstapp/index.html')    
    except KeyError: 
        request.session['bank']=0
        request.session['activities']=[]
        return render(request,'firstapp/index.html')

def process (request):
    print request.POST['action']
    if request.POST['action'] == 'farm':
        #do farm process
        request.session['activities'].append("You searched the farm")
        print request.session['activities']
        request.session['bank']+= random.randint(10,20)
    if request.POST['action'] == 'cave':
        #do cave process
        request.session['activities'].append("You searched the cave")
        request.session['bank']+= random.randint(5,10)
    if request.POST['action'] == 'house':
        #do house process
        request.session['activities'].append("You searched the house")
        request.session['bank']+= random.randint(2,5)
    if request.POST['action'] == 'casino':
        #do casion process
        request.session['activities'].append("You went to the casino casino")
        request.session['bank']+= random.randint(-50,50)
    return redirect('/')


