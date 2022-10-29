from django.contrib import admin
from .models import NewUser
from tags.models import Tag
from blogs.models import Blog
from comments.models import Comment

# Register your models here.
admin.site.register(NewUser)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Comment)
