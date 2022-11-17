from django.db import models

# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length = 30, unique = True)
    
    def __str__(self):
        return f"id: {self.id}, title: {self.title}"