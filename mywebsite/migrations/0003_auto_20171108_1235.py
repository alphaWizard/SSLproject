# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-08 12:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0002_auto_20171108_1233'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='People_profile',
            new_name='Profile',
        ),
    ]
