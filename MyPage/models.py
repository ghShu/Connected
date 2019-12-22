from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField

# Create your models here.
# Djando Models:
# https://docs.djangoproject.com/en/3.0/topics/db/models/  
class Post(models.Model):
    title = models.TextField(blank=True, null=True)
    # image = models.ImageField()  models.ImageField does not have much function
    image = ProcessedImageField(
        upload_to='static/images/posts',
        format='JPEG',
        blank=True,
        null=True
        )

    def get_absolute_url(self):
        """
        This function will be automatically called when a new post is created.
        It will redirected to the url.

        post_detail --> urls.py to find the url
        """
        return reverse("post_detail", args=[str(self.id)])