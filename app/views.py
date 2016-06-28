from django.shortcuts import render
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render_to_response
from django.template import RequestContext
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404


# import json
# import datetime
#
# from django.db.models import Q
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.core.mail import send_mail
# Create your views here.

# @login_required(login_url='/admin/login/')
# def index(request):
#     return render(request, 'index.html', {'object': 'object'})


# send_mail('Pedido de Cliente', mess_pedido,
#               'postmaster@sandbox3cb2aeaee26e40d99701d79339faccce.mailgun.org',
#               ['sac.dcher@gmail.com', 'caiodotdev@gmail.com'], fail_silently=False)

# def get_data_formated(data):
#     # replace = data.replace('/', '-')
#     date = datetime.datetime.strptime(data, '%d/%m/%Y')
#     new_d = datetime.datetime.strftime(date, '%Y-%m-%d')
#     return new_d

# Create your views here.



def index(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    
    return render_to_response('index.html', {
        'categorias': Categoria.objects.all(),
        'posts': posts
    })


def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })


def view_category(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    return render_to_response('view_categoria.html', {
        'categoria': categoria,
        'posts': Post.objects.filter(categoria=categoria)[:5]
    })
    

def contato(request):
    return render_to_response('contato.html', {},
                              context_instance=RequestContext(request))
                              

def submit_recado(request):
    data = request.POST
    try:
        recado = Recado(nome=data['nome'], email=data['email'], mensagem=data['mensagem'])
        recado.save()
        messages.success(request, 'Contato enviado com sucesso!')
        return redirect('/contato')
    except:
        messages.error(request, 'Houve algum erro.')
        return redirect('/contato')


def submit_mail(request):
    data = request.POST
    try:
        mail = MailListing(nome=data['nome'], email=data['email'])
        mail.save()
        messages.success(request, 'Email adicionado com sucesso!')
        return redirect('/')
    except:
        messages.error(request, 'Houve algum erro.')
        return redirect('/')
