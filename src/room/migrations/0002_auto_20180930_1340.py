# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-09-30 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['room_type', 'roomno']},
        ),
    ]