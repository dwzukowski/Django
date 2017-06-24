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
        check = User.usersManager.filter(email=email)
        if len(check) > 0:
            messages.append('This email is already in database, please log in')
            return (False, messages)
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
        print email
        user = User.usersManager.filter(email=email)
        print user
        if len(user) < 1:
            messages.append('Email not in database')
            return (False, messages)
        if password != user[0].password:
            messages.append('Incorrect password')
            return (False, messages)
        else:
            user=user[0].id
            return (True, user)
class SecretsManger(models.Manager):
    def post(self, message, user):
        messages=[]
        print message
        print user
        if len(message)== 0:
            messages.append('Secrets cannot be blank')
            return (False, messages)
        else:
            secret= Secret.secretsManager.create(message=message, user_id=user)
            print secret
            return (True, secret)
    def destroy(self, user, secret):
        messages=[]
        check= Secret.secretsManager.filter(user_id=user, id=secret)
        if len(check) < 1: 
            messages.append('You cannot delete other people\'s secrets!')
            return (False, messages)
        else:
            Secret.secretsManager.filter(id=secret).delete()
            return 'success'
class LikesManager(models.Manager):
    def like(self, user, secret):
        messages=[]
        check= Like.likesManager.filter(user_id=user, secret_id=secret)
        if len(check) > 0: 
            messages.append('You already liked this secret')
            return (False, messages)
        else:
            like= Like.likesManager.create(user_id=user, secret_id=secret)
            return (True, like)
class User(models.Model):
    firstName= models.CharField(max_length=255)
    lastName= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    usersManager= UsersManager()
class Secret(models.Model):
    message= models.TextField(max_length=5000)
    user= models.ForeignKey(User)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    secretsManager= SecretsManger()
class Like(models.Model):
    user= models.ForeignKey(User)
    secret= models.ForeignKey(Secret)
    created_at= models.DateTimeField(auto_now=True)
    likesManager= LikesManager()
class Comment(models.Model):
    comment= models.CharField(max_length=500)
    user= models.ForeignKey(User)
    secret= models.ForeignKey(Secret)