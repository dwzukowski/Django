# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context= {
        'courses': Course.coursesManager.all()
    }
    return render(request,'firstapp/index.html',context)
def add_course(request):
    check = Course.coursesManager.add(request.POST['name'], request.POST['description'])
    return redirect('/')
def destroy(request,id):
    context={
        'course': Course.coursesManager.get(id=id)
    }
    return render(request, 'firstapp/destroy.html', context)
def confirm_destroy(request,id):
    check = Course.coursesManager.delete(id)
    return redirect('/')