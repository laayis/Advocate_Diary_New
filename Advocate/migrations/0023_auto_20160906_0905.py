# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-06 03:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advocate', '0022_auto_20160904_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
