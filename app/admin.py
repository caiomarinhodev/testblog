from cloudinary import CloudinaryImage
from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from django.utils.text import slugify

from app.models import *


class PostForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        exclude = ['slug']


class DataEntryForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = DataEntry
        exclude = ['']


class ImagePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'is_background_home', 'is_visible',)


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'role',)


class ImagePostInline(admin.TabularInline):
    model = ImagePost


class ImageDataEntryInline(admin.TabularInline):
    model = ImageDataEntry


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


class DataEntryAdmin(admin.ModelAdmin):
    inlines = [ImageDataEntryInline, ]
    form = DataEntryForm
    list_display = ('title', 'id', 'created_at', 'published_at', 'is_visible')
    ordering = ['-created_at']


class ObservatoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'id', 'created_at')


class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'id', 'created_at')


class EmAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'id', 'created_at')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'id', 'created_at')


class CategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.slug = slugify(obj.name[:50])
        except:
            obj.slug = slugify(obj.name)
        super(CategoryAdmin, self).save_model(request, obj, form, change)


class SubCategoryAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.slug = slugify(obj.name[:50])
        except:
            obj.slug = slugify(obj.name)
        super(SubCategoryAdmin, self).save_model(request, obj, form, change)


admin.site.register(Message, MessageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(ImagePost, ImagePostAdmin)
admin.site.register(ImageDataEntry)
admin.site.register(Post, PostAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Observatory, ObservatoryAdmin)
admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Em, EmAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(DataEntry, DataEntryAdmin)
