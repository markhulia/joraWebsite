# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-21 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_individual_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='is_married',
            field=models.BooleanField(default=False),
        ),
    ]
