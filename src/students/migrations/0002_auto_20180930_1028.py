# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-30 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bedno',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='roomno',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]