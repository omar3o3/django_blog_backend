from django.contrib import admin
from .models import NewUser
from tags.models import Tag
from blogs.models import Blog
from blogs.models import UserFollowing
from comments.models import Comment
from tagBlogs.models import TagBlog

from django.contrib.auth import get_user_model

NewUser = get_user_model()

# Register your models here.
admin.site.register(NewUser)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(UserFollowing)
admin.site.register(Comment)
admin.site.register(TagBlog)
