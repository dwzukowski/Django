# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 20:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='founder',
            old_name='firstName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='founder',
            name='lastName',
        ),
    ]
