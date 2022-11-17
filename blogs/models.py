from django.db import models
from django.utils import timezone
from users.models import NewUser
# from tagBlogs.models import TagBlog

# from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(NewUser, on_delete = models.CASCADE)
    title = models.CharField(max_length = 60)
    content = models.CharField(max_length = 2500)
    # date_posted = models.DateField(default = timezone.now)
    # likes = models.PositiveIntegerField(default=0)
    
    # tags = GenericRelation(TagBlog)
    
    
    def __str__(self):
        return f"id: {self.id}, title: {self.title}, content: {self.content} user: {NewUser.objects.get(pk=self.user.id).user_name}"