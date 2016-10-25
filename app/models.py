from __future__ import unicode_literals
from cloudinary.models import CloudinaryField

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models import permalink


# Create your models here.


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
    # TODO: Mudar attr.
    categoria = models.ForeignKey(Category)
    subcategory = models.ManyToManyField(SubCategory)
    is_visible = models.BooleanField(default=True)
    author = models.ForeignKey(User, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return u'%s' % (self.title)

    # TODO: Criar metodo que gera uma descricao a partir do texto
    @permalink
    def get_absolute_url(self):
        return ('post', None, {'slug': self.slug})


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
