# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 02:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0005_auto_20161120_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='stuednt',
            new_name='student',
        ),
    ]