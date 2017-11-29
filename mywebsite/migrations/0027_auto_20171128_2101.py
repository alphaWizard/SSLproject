# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-28 21:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0026_promotion_prof'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promotion',
            name='prof',
        ),
        migrations.AddField(
            model_name='promotion',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]