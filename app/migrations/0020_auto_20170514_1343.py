# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataentry',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='dataentry',
            name='published_at',
        ),
        migrations.RemoveField(
            model_name='dataentry',
            name='text',
        ),
        migrations.AddField(
            model_name='dataentry',
            name='created',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='em',
            field=models.ForeignKey(blank=True, null=True, to='app.Em'),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='typing',
            field=models.ForeignKey(blank=True, null=True, to='app.Type'),
        ),
        migrations.AlterField(
            model_name='dataentry',
            name='instrument',
            field=models.ForeignKey(blank=True, null=True, to='app.Instrument'),
        ),
        migrations.AlterField(
            model_name='dataentry',
            name='observatory',
            field=models.ForeignKey(blank=True, null=True, to='app.Observatory'),
        ),
    ]
