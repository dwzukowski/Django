# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Book

def index(request):
    books = Book.objects.all()
    for book in books:
        print book.title, book.category    
    return render(request,'firstapp/index.html')
