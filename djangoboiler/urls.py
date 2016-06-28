"""djangoboiler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from app import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/login/$', auth_views.login),
    url(r'^$', views.index, name='index'),
    url(r'^blog/view/(?P<slug>[^\.]+).html', views.view_post, name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+).html', views.view_category, name='view_blog_category'),
    url(r'^contato', views.contato, name='contato'),
    url(r'^submit-mail', views.submit_mail, name='submit-cadastro'),
    url(r'^submit-recado', views.submit_recado, name='submit-recado')
]
