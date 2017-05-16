#!-*- conding: utf8 -*-
import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
import dropbox

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


def get_observatory(observatory):
    try:
        obs = Observatory.objects.get(key=observatory)
    except:
        obs = None
    return obs


def get_em(em):
    try:
        obs = Em.objects.get(key=em)
    except:
        obs = None
    return obs


def get_instrument(em):
    try:
        obs = Instrument.objects.get(key=em)
    except:
        obs = None
    return obs


def get_type(em):
    try:
        obs = Type.objects.get(key=em)
    except:
        obs = None
    return obs


def save_data_entry(title, movie, instrument, observatory, em, type, created_at):
    try:
        data_entry = DataEntry.objects.get(title=title, observatory=observatory)
    except:
        data_entry = DataEntry(title=title, movie=movie, instrument_key=instrument, observatory=observatory, em=em,
                               type=type, created=created_at)
        data_entry.save()
    return data_entry


def convert_date(strin):
    st_pattern = "%Y%m%d%H%M%S"
    return datetime.datetime.strptime(strin, st_pattern)


def save_image_entry(entry, url, arr):
    try:
        img = ImageDataEntry.objects.get(url=make_url(url), filename=entry.name)
    except ImageDataEntry.DoesNotExist:
        title = entry.name
        movie = url
        obs = get_observatory(arr[0])
        instrument = get_instrument(arr[1])
        em = get_em(arr[2])
        type = get_type(arr[3])
        created_at = convert_date(arr[4])
        data_entry = save_data_entry(title, movie, instrument, obs, em, type, created_at)
        img = ImageDataEntry(filename=entry.name, url=make_url(url), model=data_entry)
        img.save()
    return img


def schedule_job():
    dbx = dropbox.Dropbox('ngrUwh1dfAAAAAAAAAAAC8zBJhbb6ycu2hPNexGtMqHsmtSCK4GPlnwzLiVVEoJZ')
    for entry in dbx.files_list_folder('').entries:
        url = dbx.sharing_create_shared_link(entry.path_display).url
        arr = split_str(entry.name)
        img = save_image_entry(entry, url, arr)


def cron(request):
    schedule_job()
    return redirect('/')


def home_paginate(request):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    subcategories = SubCategory.objects.filter(is_visible=True).order_by('-created_at')
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
                                             'subcategories': subcategories,
                                             'posts': posts,
                                             'image_posts': image_posts},
                              context_instance=RequestContext(request))


def search_paginate(request):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    subcategories = SubCategory.objects.filter(is_visible=True).order_by('-created_at')
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
                                            'subcategories': subcategories,
                                            'posts': posts})


def list_category_paginate(request, slug):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    subcategories = SubCategory.objects.filter(is_visible=True).order_by('-created_at')
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
                                            'subcategories': subcategories,
                                            'posts': posts})


def list_subcategory_paginate(request, slug):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    subcategories = SubCategory.objects.filter(is_visible=True).order_by('-created_at')
    posts = Post.objects.filter(is_visible=True, subcategory=get_object_or_404(SubCategory, slug=slug)).order_by(
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
                                            'subcategories': subcategories,
                                            'posts': posts})


def view_post(request, slug):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    subcategories = SubCategory.objects.filter(is_visible=True).order_by('-created_at')
    return render_to_response('post.html', {'post': get_object_or_404(Post, slug=slug),
                                            'categories': categories,
                                            'subcategories': subcategories},
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


def team(request):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    return render_to_response('team.html', {
        'categories': categories,
        'members': TeamMember.objects.all()
    }, context_instance=RequestContext(request))


def data(request):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    return render_to_response('calendar.html', {
        'categories': categories,
        'observatories': Observatory.objects.all()
    }, context_instance=RequestContext(request))


def view_data(request, id):
    categories = Category.objects.filter(is_visible=True).order_by('-created_at')
    subcategories = SubCategory.objects.filter(is_visible=True).order_by('-created_at')
    return render_to_response('view_data.html', {'data': get_object_or_404(DataEntry, id=id),
                                                 'categories': categories,
                                                 'subcategories': subcategories},
                              context_instance=RequestContext(request))


def list_obs_data(request):
    query = request.GET
    obs = Observatory.objects.get(id=query['id'])
    entries = DataEntry.objects.first(observatory=obs, created=query['data'])
    return render_to_response('list_data.html', {'entries': entries},
                              context_instance=RequestContext(request))
