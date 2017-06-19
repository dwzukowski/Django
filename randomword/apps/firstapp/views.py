# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from random_words import RandomWords

def index(request):
    try:
        request.session['count']
        return render(request, 'firstapp/index.html')
    except: 
        request.session['count']= 0
        return render(request, 'firstapp/index.html')
def generate(request):
    if request.method=='POST':
        rw= RandomWords()
        word= rw.random_word()
        request.session['count']= request.session['count']+1
        request.session['word']= word        
        return redirect ('/')
    else:
        return redirect('/')