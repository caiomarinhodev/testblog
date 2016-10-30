from __future__ import unicode_literals
from cloudinary.models import CloudinaryField

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models import permalink


# Create your models here.
from django.template.defaultfilters import safe


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    @permalink
    def get_absolute_url(self):
        return ('category', None, {'slug': self.slug})


class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    slug = models.SlugField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    @permalink
    def get_absolute_url(self):
        return ('sub-category', None, {'slug': self.slug})


class Post(models.Model):
    title = models.CharField(max_length=150)
    text = RichTextField()
    category = models.ForeignKey(Category)
    subcategory = models.ManyToManyField(SubCategory)
    is_visible = models.BooleanField(default=True)
    author = models.ForeignKey(User, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return u'%s' % (self.title)

    def get_description(self):
        return safe(self.text[:200])

    @permalink
    def get_absolute_url(self):
        return ('view_post', None, {'slug': self.slug})


class ImagePost(models.Model):
    image = CloudinaryField('image')
    model = models.ForeignKey(Post, null=True, blank=True)
    label = models.CharField(max_length=100, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    is_background_home = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Message(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.email)


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    facebook = models.URLField(blank=True, null=True)
    googleplus = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    role = models.CharField(max_length=100)
    site = models.URLField(blank=True, null=True)
    image = CloudinaryField('image')
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Observatory(models.Model):
    name = models.CharField(max_length=100)
    key = models.CharField(max_length=3)
    is_visible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class DataEntry(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    movie = models.CharField(max_length=150, blank=True, null=True)
    intrument = models.CharField(max_length=100, blank=True, null=True)
    observatory = models.ForeignKey(Observatory)
    text = RichTextField()
    is_visible = models.BooleanField(default=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % (self.title)

    @permalink
    def get_absolute_url(self):
        return ('view_data', None, {'id': self.id})


class ImageDataEntry(models.Model):
    image = CloudinaryField('image')
    model = models.ForeignKey(DataEntry, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
