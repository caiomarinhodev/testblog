#!-*- conding: utf8 -*-
from django.shortcuts import render_to_response

from .models import *



def home(request):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    image_posts = ImagePost.objects.filter(is_background_home=True).order_by('-created_at')
    return render_to_response('index.html', {'categories':categories,
                                             'image_posts': image_posts})
