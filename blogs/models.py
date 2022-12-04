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
    created_at = models.DateTimeField(auto_now_add=True)
    
    @property
    def nyc_time(self):
        utc_date = self.created_at
        publish_date = timezone.localtime(utc_date)
        return publish_date
    
    def __str__(self):
        return f"id: {self.id}, title: {self.title}, content: {self.content[0:20]}... user: {NewUser.objects.get(pk=self.user.id).user_name} created_at: {self.created_at} , nyc_time: {self.nyc_time}"
    
    
class UserFollowing(models.Model):
    user_id = models.ForeignKey(NewUser, related_name="following", on_delete = models.CASCADE)
    following_user_id = models.ForeignKey(NewUser, related_name="followers", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"user_id: {self.user_id.user_name}, following_user_id: {self.following_user_id.user_name}"