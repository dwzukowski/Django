# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
FIRSTNAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
LASTNAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UsersManager(models.Manager):
    def add(self, firstName, lastName, email, password, confirmpassword):
        messages= []
        if not FIRSTNAME_REGEX.match(firstName):
            messages.append('First name is a required field and can only contain letters')
        if not LASTNAME_REGEX.match(lastName):
            messages.append('Last name is a required field and can only contain letters')
        if not EMAIL_REGEX.match(email):
            messages.append('Not a valid email')
        if password != confirmpassword:
            messages.append('Password does not match password confirmation')
        if len(messages) == 0:
            user= User.usersManager.create(firstName=firstName, lastName=lastName, email=email, password=password)
            return (True, user)
        return (False, messages)
    def isLoggedin(self, id):
        user= User.usersManager.get(id=id)
        return user
    def loginValidation(self, email, password):
        messages= []
        user = User.usersManager.filter(email=email)
        if len(user) < 1:
            messages.append('Email not in database')
            return (False, messages)
        if password != user[0].password:
            messages.append('Incorrect password')
            return (False, messages)
        else:
            #user= User.usersManager.get(email=email).id
            user=user[0].id
            return (True, user)
class User(models.Model):
    firstName= models.CharField(max_length=255)
    lastName= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    usersManager= UsersManager()