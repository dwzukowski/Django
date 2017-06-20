# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Message, User, Comment
def index(request):
    messages= Message.objects.all()
    comments= Comment.objects.all()
    users= User.objects.all()
    print messages
    print comments
    print users
    print messages[0].message
    #JOIN tables and retrieve last name of user who made comment id 0; user is foreign key of User class which has the attribute lastName
    print comments[0].user.lastName 
    print comments[0].text
    print comments[0].message.message

    return render(request, 'firstapp/index.html')

