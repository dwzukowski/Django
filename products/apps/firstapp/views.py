# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Product

def index(request):
    products = Product.objects.all()
    for product in products:
        print product.name
    
    return render(request,'firstapp/index.html')

# Create your views here.
