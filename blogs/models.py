from django.db import models
from django.utils import timezone
from users.models import NewUser

# Create your models here.
class Blog(models.Model):
    user = models.ForeignKey(NewUser, on_delete = models.CASCADE)
    title = models.CharField(max_length = 60)
    content = models.CharField(max_length = 2500)
    date_posted = models.DateField(default = timezone.now)
    likes = models.PositiveIntegerField(default=0)