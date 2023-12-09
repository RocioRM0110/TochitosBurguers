"""APIROCIO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import *





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index.as_view(),name='Index'),
    path('index.html',Index.as_view(),name='index'),
    path('register.html',Register.as_view(),name='register'),
    path('password.html',Password.as_view(),name='password'),
    path('about.html',About.as_view(),name='about'),
    path('blog.html',Blog.as_view(),name='blog'),
    path('contact.html',Contact.as_view(),name='contact'),
    path('recipe.html',Recipe.as_view(),name='recipe'),
    path('login.html',Login.as_view(),name='login'),
    path('dash.html',Dash.as_view(),name='dash'),
    path('products.html',Products.as_view(),name='products'),
    

]