from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from MyPage.models import ConnectedUser, Post

# forms defined here handles user inputs
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ConnectedUser
        fields = ('username', 'email', 'profile_pic')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = ConnectedUser
        fields = ('username', 'email', 'profile_pic')

# class PostPictureForm(ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'image', ]