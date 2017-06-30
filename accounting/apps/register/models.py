# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt 
from datetime import datetime
from decimal import *
NAME_REGEX = re.compile(r'^[a-zA-Z ]+ [a-zA-Z0-9_]{3,}$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]{3,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class FoundersManager(models.Manager):
    def add(self, name, email, userName, password, confirmpassword):
        messages= []
        checkusername= Founder.manager.filter(userName=userName)
        if len(checkusername) > 0:
            messages.append('This user name is already in database, please log in')
            return (False, messages)
        if len(name) < 1:
            messages.append('Name is required')
        elif len(name) < 3:
            messages.append('Name must be at least three characters') 
        if len(userName) < 1:
            messages.append('Username is required')
        elif len(userName) < 3:
            messages.append('Username must be at least three characters')
        if not NAME_REGEX.match(name):
            messages.append('Name is a required field and can only contain letters')
        if not USERNAME_REGEX.match(userName):
            messages.append('Not a valid username')
        if not EMAIL_REGEX.match(email):
            messages.append('Not a valid email')              
        if password != confirmpassword:
            messages.append('Password does not match password confirmation')
        if len(messages) == 0:
            hashedPassword= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) 
            founder= Founder.manager.create(name=name, email=email,userName=userName, password=hashedPassword)
            return (True, founder)
        return (False, messages)
    def loginValidation(self, userName, password):
        messages= []
        founder = Founder.manager.filter(userName=userName)
        if len(founder) < 1:
            messages.append('Username not found')
            return (False, messages)
        if bcrypt.hashpw(password.encode('utf-8'), founder[0].password.encode('utf-8')) != founder[0].password.encode('utf-8'):
            messages.append('Incorrect password')
            return (False, messages)
        else:
            founder= founder[0].id
            return (True, founder)
class ConcernsManager(models.Manager):
    def add(self, founder, name, description, industry, founded_at):
        messages=[]
        checkconcern= Concern.manager.filter(name=name, founder_id=founder)
        if len(checkconcern) > 0:
            messages.append('Company is already in the database')
            return False, messages
        if len(name) < 1:
            messages.append('Company name is required')
        if len(description) < 1:
            messages.append('Company description is required')
        if len(founded_at) < 1:
            messages.append('Date of founding is required')
        if len(name) < 1:
            messages.append('Company name is required')
        if len(industry) < 1:
            messages.append('Industry is required')
        clean_date= datetime.strptime(founded_at, '%Y-%m-%d')
        if clean_date > datetime.now():
            messages.append('Date of founding can\'t begin in the future')
        if len(messages) > 0: 
            return False, messages
        else: 
            concern= Concern.manager.create(founder_id=founder, name=name, description=description, industry=industry, founded_at=founded_at)
            return True, concern

class AssetsManager(models.Manager):
    def add(self, concern, assetType, description, cost, acquired_at, accDepreciation=0):
        messages=[]
        clean_date= datetime.strptime(acquired_at, '%Y-%m-%d')
        if clean_date > datetime.now():
            messages.append('Date of acquisition can\'t be in the future')
        if len(messages) > 0:
            return False, messages
        asset= Asset.manager.create(concern_id=concern, assetType_id=assetType, description=description, cost=cost, accDepreciation=accDepreciation,acquired_at=acquired_at)
        return True, asset
    def destroy(self, asset_id):
        Asset.manager.get(id=asset_id).delete()

class AssetTypesManager(models.Manager):
    def add(self, name):
        messages=[]
        if len(name) < 1:
            messages.append('type required')
            return False, messages
        newtype= AssetType.manager.create(name=name)
        return True, newtype

class LiabilityTypesManager(models.Manager):
    pass
class LiabilitiesManager(models.Manager):
    pass
class EquitiesManager(models.Manager):
    pass
class Founder(models.Model):
    name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)    
    userName= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    manager= FoundersManager()
class Concern(models.Model):
    founder= models.ForeignKey(Founder)
    name= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    industry= models.CharField(max_length=255)
    founded_at= models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    manager= ConcernsManager()
class AssetType(models.Model):
    name= models.CharField(max_length=255)
    manager= AssetTypesManager()
class Asset(models.Model):
    concern= models.ForeignKey(Concern)
    assetType= models.ForeignKey(AssetType)
    description= models.CharField(max_length=255)
    cost= models.DecimalField(max_digits=12, decimal_places=2)
    accDepreciation= models.DecimalField(max_digits=12, decimal_places=2)
    acquired_at= models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    manager= AssetsManager()
class LiabilityType(models.Model):
    name= models.CharField(max_length=255)
    manager= LiabilityTypesManager()
class Liability(models.Model):
    concern= models.ForeignKey(Concern)
    liabilityType= models.ForeignKey(LiabilityType)
    description= models.CharField(max_length=255)
    amount= models.DecimalField(max_digits=12, decimal_places=2)
    accDepreciation= models.DecimalField(max_digits=12, decimal_places=2)
    acquired_at= models.DateField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    manager= LiabilitiesManager()
class Equity(models.Model):
    concern= models.ForeignKey(Concern)
    description= models.CharField(max_length=255)
    amount= models.DecimalField(max_digits=12, decimal_places=2)
    manager= EquitiesManager()


    
