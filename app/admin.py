from base64 import b64encode

from django.contrib import admin
import pyimgur
from django.utils.text import slugify
from django import forms
from ckeditor.widgets import CKEditorWidget

from .models import *


class PostForm(forms.ModelForm):
    texto = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        exclude = ['slug']


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('titulo', 'id', 'autor', 'editado_em', 'visivel')
    list_filter = ('titulo', 'autor', 'editado_em')
    ordering = ['-editado_em']

    def save_model(self, request, obj, form, change):
        if request.FILES:
            # mudar o client id para cada cliente.
            try:
                CLIENT_ID = "cdadf801dc167ab"
                data = b64encode(request.FILES['imagem'].read())
                client = pyimgur.Imgur(CLIENT_ID)
                r = client._send_request('https://api.imgur.com/3/image', method='POST', params={'image': data})
                obj.imagem = r['link']
            except:
                if obj.imagem:
                    if 'imgur' not in obj.imagem:
                        obj.imagem = 'http://placehold.it/1024x800'
                else:
                    obj.imagem = 'http://placehold.it/1024x800'
        obj.autor = request.user
        obj.slug = slugify(obj.titulo)
        super(PostAdmin, self).save_model(request, obj, form, change)


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('tag', 'id', 'slug', 'autor', 'editado_em')
    list_filter = ('tag', 'slug', 'autor', 'editado_em')
    ordering = ['-editado_em']
    exclude = ('slug',)

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        obj.slug = slugify(obj.tag)
        super(CategoriaAdmin, self).save_model(request, obj, form, change)


class RecadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'id')
    ordering = ['-criado_em']


class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'id')
    ordering = ['-criado_em']


admin.site.register(Post, PostAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Recado, RecadoAdmin)
admin.site.register(Cadastro, CadastroAdmin)
