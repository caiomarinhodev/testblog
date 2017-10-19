from __future__ import unicode_literals
from cloudinary.models import CloudinaryField

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models import permalink

# Create your models here.
from django.template.defaultfilters import safe


class TimeStamped(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)


class Category(TimeStamped):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    is_visible = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s' % (self.name)

    @permalink
    def get_absolute_url(self):
        return ('category', None, {'slug': self.slug})


# class SubCategory(TimeStamped):
#     class Meta:
#         verbose_name = "SubCategory"
#         verbose_name_plural = "SubCategories"
#
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     slug = models.SlugField(unique=True, blank=True, null=True)
#     name = models.CharField(max_length=100, unique=True)
#     is_visible = models.BooleanField(default=True)
#
#     def __unicode__(self):
#         return u'%s' % (self.name)
#
#     @permalink
#     def get_absolute_url(self):
#         return ('sub-category', None, {'slug': self.slug})


class Post(TimeStamped):
    title = models.CharField(max_length=150)
    text = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # subcategory = models.ManyToManyField(SubCategory)
    is_visible = models.BooleanField(default=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return u'%s' % (self.title)

    def get_description(self):
        return safe(self.text[:200])

    @permalink
    def get_absolute_url(self):
        return ('view_post', None, {'slug': self.slug})


class ImagePost(TimeStamped):
    class Meta:
        verbose_name = "ImagePost"
        verbose_name_plural = "ImagePosts"

    image = CloudinaryField('image')
    model = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)
    label = models.CharField(max_length=100, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    is_background_home = models.BooleanField()


class Message(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.email)
