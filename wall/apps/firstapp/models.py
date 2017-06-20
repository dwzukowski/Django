# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class User(models.Model):
    firstName= models.CharField(max_length=255)
    lastName= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now=True)
    updated_at= models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    user= models.ForeignKey(User)
    message= models.TextField()
    created_at= models.DateTimeField(auto_now=True)
    updated_at= models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    message= models.ForeignKey(Message) 
    user= models.ForeignKey(User)
    text= models.TextField()
    created_at= models.DateTimeField(auto_now=True)
    updated_at= models.DateTimeField(auto_now_add=True)
