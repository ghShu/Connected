"""
This module handles the requests from Connected/urls.py.
"""

from django.shortcuts import render
from django.views.generic import (TemplateView, 
                                  ListView,
                                  DetailView)
from django.views.generic.edit import (CreateView,
                                       UpdateView,
                                       DeleteView)
from django.contrib.auth.forms import UserCreationForm
from django.urls import (reverse,
                         reverse_lazy)                                       

from MyPage.models import Post

# Create your views here.
# Django views: 
# https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/ 
# Django has prepared many class-based views for common use cases

class HelloDjango(TemplateView):
    template_name = 'test.html'


class PostsView(ListView):
    """
    https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView
    """
    model = Post                 # Connect View with Model
    template_name = 'index.html' # This connects View with Template


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    
    # fields should come from model
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title']


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    # Django does not allow reverse while deletting
    # Therefore, reverse_lazy should be used
    # https://docs.djangoproject.com/en/3.0/ref/urlresolvers/#reverse-lazy 
    success_url = reverse_lazy("posts")    


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')