# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]