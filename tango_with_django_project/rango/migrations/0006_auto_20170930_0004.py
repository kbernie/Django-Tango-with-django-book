# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-09-30 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20170929_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.URLField(),
        ),
    ]