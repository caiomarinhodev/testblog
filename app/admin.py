from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.utils.text import slugify

from app.models import *


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        exclude = ['slug']


class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'is_background_home', 'is_visible',)


class ImagePostInline(admin.TabularInline):
    model = ImagePost


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')


class PostAdmin(admin.ModelAdmin):
    inlines = [ImagePostInline, ]
    form = PostForm
    list_display = ('title', 'id', 'created_at', 'published_at', 'is_visible', 'author')
    ordering = ['-created_at']

    def save_model(self, request, obj, form, change):
        obj.autor = request.user
        try:
            obj.slug = slugify(obj.title[:50])
        except:
            obj.slug = slugify(obj.title)
        super(PostAdmin, self).save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible',)

    def save_model(self, request, obj, form, change):
        try:
            obj.slug = slugify(obj.name[:50])
        except:
            obj.slug = slugify(obj.name)
        super(CategoryAdmin, self).save_model(request, obj, form, change)


admin.site.register(Message, MessageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ImagePost, ImagePostAdmin)
admin.site.register(Post, PostAdmin)
