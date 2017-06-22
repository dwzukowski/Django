# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'firstapp/index.html')
def register(request):
    check= User.usersManager.add(request.POST['firstName'], request.POST['lastName'],request.POST['email'], request.POST['password'], request.POST['confirmpassword'])
    if check[0]== True:
        request.session['loggedinUser']= check[1].id
        print check[1]
        print request.session['loggedinUser']
        return redirect('/success')
    else:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')

def success(request):
    if not 'loggedinUser' in request.session:
        return redirect('/')
    else:
        check= User.usersManager.isLoggedin(request.session['loggedinUser'])
        context={
            'user': check 
        }
        return render(request,'firstapp/success.html',context)
def login(request):
    check= User.usersManager.loginValidation(request.POST['email'],request.POST['password'])
    if check[0]== True:
        print check[1]
        request.session['loggedinUser']= check[1]
        return redirect('/success')
    else:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
