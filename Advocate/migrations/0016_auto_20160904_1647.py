# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 11:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Advocate', '0015_auto_20160904_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='case_stage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Advocate.CaseStage'),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Advocate.CaseType'),
        ),
        migrations.AlterField(
            model_name='case',
            name='court_of',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Advocate.CourtOf'),
        ),
    ]
