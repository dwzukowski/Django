# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User, Book, Review, Author
from django.contrib import messages
import bcrypt 
def index(request):
    return render(request, 'firstapp/index.html')
def register(request):
    check= User.usersManager.add(request.POST['firstName'], request.POST['lastName'], request.POST['userName'], request.POST['email'], request.POST['password'], request.POST['confirmpassword'])
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
    else:
        request.session['loggedinUser']= check[1].id
        return redirect('/books')

def login(request):
    check= User.usersManager.loginValidation(request.POST['userName'], request.POST['password'])
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
    else:
        request.session['loggedinUser']= check[1]
        return redirect('/books')
def books(request):
    if not 'loggedinUser' in request.session:
        messages.add_message(request, messages.ERROR, 'Please sign in')
        return redirect('/')
    else:
        context={
            #returns the four most recent reviews
            'reviews': Review.reviewsManager.order_by('-created_at')[:4],
        }
        return render(request, 'firstapp/books.html',context)
def logout(request):
    request.session.clear()
    return redirect('/')
def addbook(request):
    if not 'loggedinUser' in request.session:
        messages.add_message(request, messages.ERROR, 'Please sign in')
        return redirect('/')
    else:
        context={
            'authors': Author.authorsManager.all().order_by('name'),
        }
        return render(request, 'firstapp/addbook.html', context)
def addreview(request):
    if len(request.POST['newauthor']) > 0:
        checkauthor= Author.authorsManager.add(request.POST['newauthor'])
    else:
        checkauthor= (True, Author.authorsManager.get(id=request.POST['existingauthor']))
    if not checkauthor[0]:
        for message in checkauthor[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/books/addbook')
    checkbook= Book.booksManager.add(request.POST['title'], checkauthor[1].id)
    if not checkbook[0]:
        for message in checkbook[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/books/addbook')
    checkreview= Review.reviewsManager.add(request.POST['content'], request.POST['rating'], request.session['loggedinUser'], checkbook[1].id)
    if not checkreview[0]:
        for message in checkreview[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/books/addbook')
    return redirect('/books/addbook/{}'.format(checkbook[1].id))
def showreviews(request, book_id):
    context={
        'reviews': Review.reviewsManager.filter(book_id=book_id).order_by('-created_at'),
    }
    return render(request, 'firstapp/showreview.html', context)
