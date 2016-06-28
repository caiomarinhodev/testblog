from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models import permalink

# Create your models here.


class Categoria(models.Model):
    tag = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, db_index=True)
    autor = models.ForeignKey(User, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):  # __unicode__ on Python 2
        return str(self.tag)

    def __unicode__(self):
        return u'%s' % (self.tag)
        
    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })
        

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = RichTextField()
    categoria = models.ManyToManyField(Categoria)
    imagem = models.ImageField(blank=True, null=True)
    autor = models.ForeignKey(User, null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)
    visivel = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.titulo)

    def __unicode__(self):
        return u'%s' % (self.titulo)
        
    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })
        

class Recado(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mensagem = models.TextField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.nome) + '-' + str(self.email)

    def __unicode__(self):
        return u'%s' % (self.nome)


class Cadastro(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return str(self.nome) + '-' + str(self.email)

    def __unicode__(self):
        return u'%s' % (self.nome)
    


