# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import random

def toindex(request):
    User.objects.create_user(first_name="Mike", last_name="Hannon", username=str(random.randint(0,100)))
    users= User.objects.all()
    return render(request, "testUser/index.html", {'users':users})
