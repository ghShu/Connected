from django.contrib import admin
from MyPage.models import (Post, 
                           ConnectedUser,
                           Like)

# Register your models here.
admin.site.register(Post)
admin.site.register(ConnectedUser)
admin.site.register(Like)
