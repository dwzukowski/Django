# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class CoursesManager(models.Manager):
    def add(self, name, description):
        messages= []
        if len(name) < 2:
            messages.append('Courses must have a name')
        if len(description) < 2:
            messages.append('Please provide a brief description of the course')
        if len(messages) == 0:
            course= Course.coursesManager.create(name=name, description= description)
            return (True, course)
        else:
            return (False, messages)
    def delete(self, id):
        course= Course.coursesManager.get(id=id).delete()
        return (True, course)
        
class Course(models.Model):
    name= models.CharField(max_length=255)
    description= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    coursesManager= CoursesManager()


