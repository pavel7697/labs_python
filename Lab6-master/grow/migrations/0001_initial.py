# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pulpit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('year', models.PositiveIntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('third_name', models.CharField(max_length=30)),
                ('phone', models.PositiveIntegerField(max_length=11)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
