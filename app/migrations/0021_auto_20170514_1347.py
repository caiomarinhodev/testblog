# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20170514_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataentry',
            old_name='typing',
            new_name='type',
        ),
        migrations.AddField(
            model_name='dataentry',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 14, 16, 47, 12, 320098, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataentry',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 14, 16, 47, 18, 530848, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dataentry',
            name='text',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
