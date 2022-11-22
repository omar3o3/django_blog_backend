from django.db import models
from blogs.models import Blog
from users.models import NewUser

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(NewUser, on_delete = models.CASCADE)
    content =  models.CharField(max_length = 500)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)
    
    
    def __str__(self):
        return f"id: {self.id}, blog: {self.blog.id}, user: {self.user.user_name}, content: {self.content}"