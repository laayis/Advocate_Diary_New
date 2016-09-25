# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-04 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Advocate', '0019_auto_20160904_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('case_no', models.CharField(max_length=100, unique=True)),
                ('filling_date', models.DateField()),
                ('appearing_lawyer', models.CharField(max_length=500)),
                ('opposite_lawyer', models.CharField(blank=True, max_length=500)),
                ('fees', models.FloatField(blank=True, default=0.0)),
                ('remarks', models.TextField(blank=True)),
                ('prev_date', models.DateField()),
                ('next_date', models.DateField(blank=True, null=True)),
                ('fav', models.BooleanField(default=False, editable=False)),
                ('archived', models.BooleanField(default=False, editable=False)),
                ('confirmation', models.CharField(choices=[(0, 'Canceled'), (1, 'Pending'), (2, 'Confirmed')], default='Pending', editable=False, max_length=10)),
                ('case_stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Advocate.CaseStage')),
                ('case_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Advocate.CaseType')),
                ('court_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Advocate.CourtOf')),
            ],
        ),
    ]