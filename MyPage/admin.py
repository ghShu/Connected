from django.contrib import admin
from MyPage.models import (Post, 
                           ConnectedUser,
                           Like,
                           Comment,
                           UserConnection)

# Register models:
# https://docs.djangoproject.com/en/3.0/ref/contrib/admin/#django.contrib.admin.StackedInline
# https://stackoverflow.com/questions/4890981/django-admin-stackedinline-customisation

class CommentInline(admin.StackedInline):
    model = Comment

class LikeInline(admin.StackedInline):
    model = Like

class FollowingInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'creator'

class FollowerInline(admin.StackedInline):
    model = UserConnection
    fk_name = 'following'

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
        LikeInline,
    ]

class UserAdmin(admin.ModelAdmin):
    inlines = [
        FollowerInline,
        FollowingInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(ConnectedUser, UserAdmin)
admin.site.register(UserConnection)
admin.site.register(Like)
admin.site.register(Comment)
