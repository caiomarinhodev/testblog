#!-*- conding: utf8 -*-
import datetime

from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from .models import *


def split_str(str):
    arr = str.split('_')
    if arr[-1].endswith('.png') or arr[-1].endswith('.jpg') or arr[-1].endswith('.PNG') or arr[-1].endswith('.JPG'):
        arr[-1] = arr[-1][:-4]
    elif arr[-1].endswith('.jpeg'):
        arr[-1] = arr[-1][:-5]
    return arr


def make_url(url):
    if url.endswith('?dl=0'):
        url = url[:-5]
    return url.replace('www.dropbox', 'dl.dropboxusercontent')


def convert_date(strin):
    st_pattern = "%Y%m%d%H%M%S"
    return datetime.datetime.strptime(strin, st_pattern)


def home_paginate(request):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    image_posts = ImagePost.objects.filter(is_background_home=True).order_by('-created_at')
    posts = Post.objects.filter(is_visible=True).order_by('-created_at')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {'categories': categories,
                                             'posts': posts,
                                             'image_posts': image_posts},
                              context_instance=RequestContext(request))


def search_paginate(request):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    posts = Post.objects.filter(is_visible=True).order_by('-created_at')
    if 'q' in request.GET:
        posts = Post.objects.filter(text__icontains=request.GET['q'], is_visible=True).order_by('-created_at')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render_to_response('blog.html', {'categories': categories,
                                            'q': request.GET['q'],
                                            'posts': posts})


def list_category_paginate(request, slug):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    posts = Post.objects.filter(is_visible=True, category=get_object_or_404(Category, slug=slug)).order_by(
        '-created_at')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render_to_response('blog.html', {'categories': categories,
                                            'category': slug,
                                            'posts': posts})


#
# def list_subcategory_paginate(request, slug):
#     categories = Category.objects.filter(is_visible=True).order_by('-created_at')
#     posts = Post.objects.filter(is_visible=True).order_by(
#         '-created_at')
#     paginator = Paginator(posts, 6)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         posts = paginator.page(paginator.num_pages)
#     return render_to_response('blog.html', {'categories': categories,
#                                             'category': slug,
#                                             'posts': posts})


def view_post(request, slug):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    return render_to_response('post.html', {'post': get_object_or_404(Post, slug=slug),
                                            'categories': categories},
                              context_instance=RequestContext(request))


def contact(request):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    return render_to_response('contact.html', {
        'categories': categories
    }, context_instance=RequestContext(request))


def submit_message(request):
    data = request.POST
    name = data.get('name')
    message = data.get('message')
    email = data.get('email')
    try:
        objeto = Message(name=name, email=email, message=message)
        objeto.save()
        messages.success(request, 'Message sent successfully!')
        return redirect('/')
    except:
        messages.error(request, 'There was an error.')
        return redirect('/')


def submit_mail_newsletter(request):
    data = request.POST
    send_mail("You're Welcome!", 'Hello, \n Thank you for registering on our website.',
              'postmaster@sandbox3cb2aeaee26e40d99701d79339faccce.mailgun.org',
              [data['email']], fail_silently=False)
    try:
        # mail = Cadastro(nome=data['nome'], email=data['email'])
        # mail.save()
        messages.success(request, "You're welcome!")
        return redirect('/')
    except:
        messages.error(request, 'Try Again.')
        return redirect('/')
