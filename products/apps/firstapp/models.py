# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name= models.CharField(max_length=255)
    description= models.CharField(max_length=255)
    weight= models.IntegerField()
    price= models.IntegerField()
    cost= models.IntegerField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
