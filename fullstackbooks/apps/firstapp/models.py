# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class BooksManager(models.Manager):
    def add(self, title, author, category):
        messages=[]
        if len(title) < 2:
            messages.append('Title cannot be blank')
        if len(author) < 2: 
            messages.append('Enter an author')
        if len(category) < 2:
            messages.append('Enter a category')
        if len(messages) > 0:
            return (False, messages)
        else: 
            book= Book.booksManager.create(title=title, author= author, category= category)
            return (True, book)
class Book(models.Model):
    title= models.CharField(max_length=255)
    author= models.CharField(max_length=255)
    category= models.CharField(max_length=255)
    booksManager= BooksManager()




# Create your models here.
