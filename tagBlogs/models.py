from django.db import models
from tags.models import Tag
from blogs.models import Blog

# Create your models here.
class TagBlog(models.Model):
    tag_id = models.ForeignKey(Tag, on_delete = models.PROTECT)
    blog_id = models.ForeignKey(Blog, on_delete = models.PROTECT)
    
    def __str__(self):
        return f"id: {self.id}, tag_id: {self.blog_id.id}, blog_id: {self.blog_id.id}"