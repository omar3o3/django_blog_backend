from rest_framework import serializers
from .models import TagBlog
# from users.models import NewUser

class TagBlogSerializer(serializers.ModelSerializer):
    
    
        class Meta:
            model = TagBlog
            # fields = ['title', 'content', 'id', 'user']
            # fields = "__all__"
            fields = ['tag_id', 'blog_id']