# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='user',
        ),
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(to='authentication.User'),
        ),
    ]
