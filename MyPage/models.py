import os
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse
from imagekit.models import ProcessedImageField

# Create models:
# Need to tell Django to not use the default user models, but this one.
# Do this in settings.py
class ConnectedUser(AbstractUser):
    profile_pic = ProcessedImageField(
        upload_to ='static/images/profiles',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True 
    )

    def get_connections(self):
        connections = UserConnection.objects.filter(creator=self)
        return connections

    def get_followers(self):
        followers = UserConnection.objects.filter(following=self)
        return followers

    def is_followed_by(self, user):
        followers = UserConnection.objects.filter(following=self)
        return followers.filter(creator=user).exists()

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])

    def __str__(self):
        return self.username


class UserConnection(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey( # A ForeignKey indicates Many-to-One relationship
        ConnectedUser,           # ForeignKey is ConnectedUser
        on_delete=models.CASCADE,
        related_name='friendship_creator_set'
    )
    following = models.ForeignKey(
        ConnectedUser,
        on_delete=models.CASCADE,
        related_name='friend_set'
    )

    def __str__(self):
        return ' '.join([self.creator.username, 'follows', self.following.username]) 

class Post(models.Model):
    """
    General post model 
    Djando Models:
    https://docs.djangoproject.com/en/3.0/topics/db/models/  
    """
    author = models.ForeignKey( # A foreignKey indicates a Many-T-One relationship
        ConnectedUser,         # ForeignKey is Connected User
        blank=True,
        null=True,
        on_delete=models.CASCADE,  # remove author profile will delete all his/her posts
        related_name='posts'    # we can use author.posts to get all posts belong to this user
                                # also in user_profile.html, object.posts list all posts related to certain user
    )
    title = models.TextField(blank=True, null=True)
    # image = models.ImageField()  models.ImageField does not have much function
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
        )

    posted_on = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    def __str__(self):
        return self.title

    def get_like_count(self):
        return self.likes.count()
    
    def get_comment_count(self):
        return self.comments.count()

    def get_absolute_url(self):
        """
        This function will be automatically called when a new post is created.
        It will redirected to the url.

        post_detail --> urls.py to find the url
        """
        return reverse("post_detail", args=[str(self.id)])


class Like(models.Model):
    """
    Model for Like relationship
    Like will be processed in Post to incorperate Likes
    related_name will find all posts related to a certain post
    use case: collect all likes for one post
    """
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name='likes'
    )

    user = models.ForeignKey(
        ConnectedUser,
        on_delete=models.CASCADE,
        related_name='likes'
    )

    class Meta:
        # one user can only like a post once
        unique_together = ['post', 'user']
    
    def __str__(self):
        return 'Like:' + self.user.username + ' likes ' + self.post.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name='comments')

    user = models.ForeignKey(
        ConnectedUser, 
        on_delete=models.CASCADE
    )
    
    comment = models.CharField(max_length=100)
    posted_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.comment
