#!-*- conding: utf8 -*-
from django.shortcuts import render_to_response, get_object_or_404, render
from django.template import RequestContext

from .models import *


def home(request):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    image_posts = ImagePost.objects.filter(is_background_home=True).order_by('-created_at')
    posts = Post.objects.filter(is_visible=True).order_by('-created_at')
    return render_to_response('index.html', {'categories': categories,
                                             'posts': posts,
                                             'image_posts': image_posts})


def search(request, query):
    pass


def view_post(request, slug):
    return render_to_response('post.html', {'projeto': get_object_or_404(Post, slug=slug)},
                              context_instance=RequestContext(request))


def submit_message(request):
    data = request.POST
    name = data.get('name')
    message = data.get('message')
    email = data.get('email')
    objeto = Message(name=name, email=email, message=message)
    try:
        objeto.save()
    except Exception:
        return render(request, 'base.html', {'error': 'Algum dado informado esta invalido.'})
    return render(request, 'base.html', {'success': 'Mensagem enviada!'})
