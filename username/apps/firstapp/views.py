# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def index(request):
    return render(request, 'firstapp/index.html')

def add_user(request):
    #print request.POST['username']
    check= User.usersmanager.add(request.POST['username'])
    print check[1]
    if check[0] == False:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
    else:
        messages.add_message(request, messages.SUCCESS, 'You successfully registered!')
    return redirect('/')
