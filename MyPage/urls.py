"""Connected URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
This is project-level url settings. Idealy, we can have app-level urls as well.
At project level, this urls.py can connect app-level urls together.
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from MyPage.views import (
    HelloDjango, 
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    SignUp,
    addLike,
    addComment
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    # use <int:pk> as primary key to search specific item in database
    # The primary key will be passed in URL
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    # path('posts/1', PostDetailView.as_view(), name='post_detail'), 
    path('post/new/', PostCreateView.as_view(), name='make_post'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('user_profile/<int:pk>/', UserProfile.as_view(), name='profile'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
    path('togglefollow', toggleFollow, name='togglefollow'),
    path('like', addLike, name='addLike'),
    path('comment', addComment, name='addComment'),
    path('hello', HelloDjango.as_view(), name='hellodjango'),
    path('auth/signup', SignUp.as_view(), name='signup'),
]


