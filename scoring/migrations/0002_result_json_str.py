# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='Json_Str',
            field=models.CharField(default=['a', 'b', 'c', 'd'], max_length=1000),
            preserve_default=False,
        ),
    ]
