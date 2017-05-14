# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_type'),
    ]

    operations = [
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
            name='instrument_key',
            field=models.ForeignKey(blank=True, null=True, to='app.Instrument'),
        ),
        migrations.AddField(
            model_name='dataentry',
            name='type',
            field=models.ForeignKey(blank=True, null=True, to='app.Type'),
        ),
    ]
