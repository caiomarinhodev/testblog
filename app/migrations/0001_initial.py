# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import cloudinary.models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(unique=True, blank=True, null=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('image', cloudinary.models.CloudinaryField(verbose_name='image', max_length=255)),
                ('label', models.CharField(max_length=100, blank=True, null=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('is_background_home', models.BooleanField()),
            ],
            options={
                'verbose_name': 'ImagePost',
                'verbose_name_plural': 'ImagePosts',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, blank=True, null=True)),
                ('email', models.EmailField(max_length=254, blank=True, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('text', ckeditor.fields.RichTextField()),
                ('is_visible', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
                ('author', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='app.Category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='imagepost',
            name='model',
            field=models.ForeignKey(blank=True, null=True, to='app.Post'),
        ),
    ]
