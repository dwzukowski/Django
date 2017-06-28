# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Founder, Concern, Asset, Liability, Equity
import bcrypt 

def index(request):
    return render(request, 'register/index.html')
def register(request):
    check= Founder.manager.add(request.POST['name'], request.POST['email'],request.POST['userName'], request.POST['password'], request.POST['confirmpassword'])
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
    else:
        request.session['loggedinUser']= check[1].id
        return redirect('/company')
def company(request):
    if not 'loggedinUser' in request.session:
        messages.add_message(request, messages.ERROR, 'Please sign in')
        return redirect('/')
    else:
        context={
            'founder': Founder.manager.get(id=request.session['loggedinUser']),
            'concerns': Concern.manager.filter(founder_id=request.session['loggedinUser'])
        }
        print context
        print context['concerns'][0].founder.name
        return render(request, 'register/company.html', context)
def logout(request):
    request.session.clear()
    return redirect('/')
def login(request):
    check= Founder.manager.loginValidation(request.POST['userName'], request.POST['password'])
    print check
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
    else:
        request.session['loggedinUser']= check[1]
        return redirect('/company')
def newconcern(request):
    check= Concern.manager.add(request.session['loggedinUser'], request.POST['name'], request.POST['description'], request.POST['industry'], str(request.POST['founded_at']))
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/company')
    request.session['loggedinConcern']= check[1].id
    return redirect('/company')