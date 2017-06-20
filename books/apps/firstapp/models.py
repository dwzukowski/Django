# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=255)
    author= models.CharField(max_length=255)
    published= models.DateField(auto_now_add=True)
    category= models.CharField(max_length=255)


