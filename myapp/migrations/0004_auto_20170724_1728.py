# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='day',
            field=models.CharField(default=0.0, max_length=3),
        ),
    ]
