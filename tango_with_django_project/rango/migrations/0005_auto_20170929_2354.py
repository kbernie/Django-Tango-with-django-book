# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-29 23:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20170928_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
