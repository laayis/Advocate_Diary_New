# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-03 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advocate', '0009_auto_20160904_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_no',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
