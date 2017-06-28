# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt 

def index(request):
    return render(request, 'firstapp/index.html')
def register(request):
    check= User.usersManager.add(request.POST['name'], request.POST['userName'], request.POST['password'], request.POST['confirmpassword'])
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
            'users': User.usersManager.all(),
        }
        return render(request, 'firstapp/company.html', context)
def logout(request):
    request.session.clear()
    return redirect('/')
def login(request):
    check= User.usersManager.loginValidation(request.POST['userName'], request.POST['password'])
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
    else:
        request.session['loggedinUser']= check[1]
        return redirect('/company')
