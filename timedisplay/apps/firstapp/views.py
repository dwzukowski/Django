# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    time = datetime.now()
    #time = datetime.utcnow()
    print time
    request.session['now']= str(time)
    return render(request, 'firstapp/index.html')
