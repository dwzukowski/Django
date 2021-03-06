# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_concern_industry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='accDepreciation',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='asset',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='equity',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='liability',
            name='accDepreciation',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='liability',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
