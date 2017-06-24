# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, Secret, Like, Comment
from django.contrib import messages
from django.db.models import Count

def index(request):
    return render(request, 'firstapp/index.html')
def register(request):
    check= User.usersManager.add(request.POST['firstName'], request.POST['lastName'], request.POST['email'], request.POST['password'], request.POST['confirmpassword'])
    if check[0]== True:
        request.session['loggedinUser']= check[1].id
        return redirect('/secrets')
    else:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
    return redirect('/')
def login(request):
    check= User.usersManager.loginValidation(request.POST['email'], request.POST['password']) 
    if check[0]== True:
        request.session['loggedinUser']= check[1]
        return redirect('/secrets')
    else:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
def secrets(request):
    #prevent users from accessing secrets without being logged in. Two checks handle 1) error due to no defined session variable and 2) session variable of False due to prior logout
    if not 'loggedinUser' in request.session or not request.session['loggedinUser']:
        return redirect('/')
    else:
        #secrets= Secret.secretsManager.all()
        #likes= Like.likesManager.all()
        #likescount=[]
        #for secret in secrets:
            #likescount.append(Like.likesManager.filter(secret_id=secret))
            #likescount.append(Like.likesManager.filter(secret_id=secret).count())
        #print Like.likesManager.filter(secret_id=2).count()
        context={
            #annotate counts number of likes 
            'secrets': Secret.secretsManager.all().annotate(Count('like')),
            'likes': Like.likesManager.all(),
            #'count': Secret.secretsManager.all().annotate(Count('like'))
        }
        #print context['count'][2].id
        #print context['count'][2].like__count
        #'count': Secret.secretsManager.annotate(Count('message'))       
        #print context['count'][1].id
        #print context['count'][1].message__id
        #print context['secrets'][1].message
        return render(request, 'firstapp/secrets.html', context)
def logout(request):
    request.session['loggedinUser']= False
    return redirect('/')
def postsecret(request):
    check= Secret.secretsManager.post(request.POST['secret'],request.session['loggedinUser'])
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/secrets')
    else:
        return redirect('/secrets')
def likesecret(request, secretid):
    check= Like.likesManager.like(request.session['loggedinUser'], secretid)
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
    return redirect('/secrets')
def deletesecret(request, secretid):
    check= Secret.secretsManager.destroy(request.session['loggedinUser'], secretid)
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
    return redirect('/secrets')