# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-19 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_imagedataentry_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagedataentry',
            name='filename',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]