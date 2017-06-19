# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random

def index(request):
    return render(request, 'firstapp/index.html')


def process(request, number):
    if number < 6 and number > 0:
        context={
            'number':number
        }
        return render(request, 'firstapp/show.html',context)
    else:
        number= random.randint(1,5)
        context={
            'number':number
        }
        return render(request, 'firstapp/show.html',context)