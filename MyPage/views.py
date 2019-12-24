"""
This module handles the requests from Connected/urls.py.
"""

from annoying.decorators import ajax_request
from django.shortcuts import render
from django.views.generic import (TemplateView, 
                                  ListView,
                                  DetailView)
from django.views.generic.edit import (CreateView,
                                       UpdateView,
                                       DeleteView)
                                
# from django.contrib.auth.forms import UserCreationForm
from MyPage.forms import CustomUserCreationForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import (reverse,
                         reverse_lazy)                                       

from MyPage.models import Post, ConnectedUser, Like, Comment

# Create your views here.
# Django views: 
# https://docs.djangoproject.com/en/3.0/ref/class-based-views/base/ 
# Django has prepared many class-based views for common use cases

class HelloDjango(TemplateView):
    template_name = 'test.html'


class PostListView(ListView):
    """
    https://docs.djangoproject.com/en/3.0/ref/class-based-views/generic-display/#django.views.generic.list.ListView
    """
    model = Post                 # Connect View with Model
    template_name = 'home.html'  # This connects View with Template


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    # fields should come from model
    fields = '__all__'
    login_url = 'login'


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
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


@ajax_request
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)   # id also works
    try:
        like = Like(post=post, user=request.user)
        like.save()
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0
    
    return {
        'result': result,
        'post_pk': post_pk
    }


@ajax_request
def addComment(request):
    comment_text = request.POST.get('comment_text')
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    commenter_info = {}

    try:
        comment = Comment(comment=comment_text, user=request.user, post=post)
        comment.save()

        username = request.user.username

        commenter_info = {
            'username': username,
            'comment_text': comment_text
        }

        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'post_pk': post_pk,
        'commenter_info': commenter_info
    }