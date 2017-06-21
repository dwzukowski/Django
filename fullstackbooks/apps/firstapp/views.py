# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Book, BooksManager
from django.contrib import messages

def index(request):
    context={
        'books': Book.booksManager.all()
    }
    return render(request, 'firstapp/index.html',context)

def add_book(request):
    check= Book.booksManager.add(request.POST['title'], request.POST['author'], request.POST['category'])
    print check
    print check[1]
    if check[0] == False:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
    return redirect('/')
