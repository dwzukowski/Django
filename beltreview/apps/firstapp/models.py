# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re
import bcrypt 
FIRSTNAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
LASTNAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UsersManager(models.Manager):
    def add(self, firstName, lastName, userName, email, password, confirmpassword):
        messages= []
        checkemail = User.usersManager.filter(email=email)
        checkusername= User.usersManager.filter(userName=userName)
        if len(checkemail) > 0:
            messages.append('This email is already in database, please log in')
            return (False, messages)
        if len(checkusername) > 0:
            messages.append('This user name is already in database, please log in')
            return (False, messages)
        if not FIRSTNAME_REGEX.match(firstName):
            messages.append('First name is a required field and can only contain letters')
        if not LASTNAME_REGEX.match(lastName):
            messages.append('Last name is a required field and can only contain letters')
        if not EMAIL_REGEX.match(email):
            messages.append('Not a valid email')
        if len(userName) < 1:
            messages.append('Username is required')
        if password != confirmpassword:
            messages.append('Password does not match password confirmation')
        if len(messages) == 0:
            hashedPassword= bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()) 
            user= User.usersManager.create(firstName=firstName, lastName=lastName,userName=userName, email=email, password=hashedPassword)
            return (True, user)
        return (False, messages)
    def loginValidation(self, userName, password):
        messages= []
        user = User.usersManager.filter(userName=userName)
        if len(user) < 1:
            messages.append('Username not found')
            return (False, messages)
        if bcrypt.hashpw(password.encode('utf-8'), user[0].password.encode('utf-8')) != user[0].password.encode('utf-8'):
            messages.append('Incorrect password')
            return (False, messages)
        else:
            user= user[0].id
            return (True, user)
class BooksManager(models.Manager):
    def add(self, title, author):
        messages= []
        checkbook = Book.booksManager.filter(title=title, author_id=author)
        if len(title) < 2:
            messages.append('Book title is a mandatory field')
            return (False, messages)
        if len(checkbook) == 1:
            book= Book.booksManager.get(title=title)
            return (True, book)
        else:
            book= Book.booksManager.create(title=title, author_id=author)
            return (True, book)            
class AuthorsManager(models.Manager):
    def add(self, author):
        messages=[]
        checkauthor= Author.authorsManager.filter(name= author)
        if len(checkauthor) > 0:
            messages.append('This author is already in database, please select from dropdown')
        if len(messages) == 0:
            author= Author.authorsManager.create(name=author) 
            return (True, author)
        else:
            return (False, messages)
class ReviewsManager(models.Manager):
    def add(self, content, rating, user, book):
        if len(content) < 2:
            messages.append('Review cannot be blank')
            return (False, messages)
        review= Review.reviewsManager.create(content=content, rating=rating, user_id=user, book_id=book)
        return (True, review) 
class User(models.Model):
    firstName= models.CharField(max_length=255)
    lastName= models.CharField(max_length=255)
    userName= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    usersManager= UsersManager()
class Author(models.Model):
    name= models.CharField(max_length=255)
    authorsManager= AuthorsManager()
class Book(models.Model):
    title= models.CharField(max_length=255)
    author= models.ForeignKey(Author)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    booksManager= BooksManager()
class Review(models.Model):
    content= models.TextField(max_length=5000)
    rating= models.IntegerField()
    user= models.ForeignKey(User)
    book= models.ForeignKey(Book)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    reviewsManager= ReviewsManager()

