from django.db import models
from blogs.models import Blog
from users.models import NewUser

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(NewUser, on_delete = models.CASCADE)
    content =  models.CharField(max_length = 150)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)