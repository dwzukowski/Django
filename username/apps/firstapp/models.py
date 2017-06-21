# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re 
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9._-]{8,28}$')

class UsersManager(models.Manager):
        def add(self, username):
            messages=[]
            if not USERNAME_REGEX.match(username):
                messages.append('Username must be between 8 and 28 characters long. Letters, numbers, and _ or - only')
            if len(messages) == 0:
                user= User.usersmanager.create(username=username)
                return (True, user)
            else:
                return (False, messages)

class User(models.Model):
    username= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    usersmanager= UsersManager()
# Create your models here.
