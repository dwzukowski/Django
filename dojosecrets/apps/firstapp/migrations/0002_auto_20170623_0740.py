# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 11:40
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='secret',
            managers=[
                ('secretsManager', django.db.models.manager.Manager()),
            ],
        ),
    ]
