from rest_framework import serializers
from .models import TagBlog
# from users.models import NewUser
from tags.serializers import TagSerializer
from tags.models import Tag

class TagBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagBlog
        fields = ['tag_id', 'blog_id']
        
class CustomTagBlogSerializer(serializers.ModelSerializer):

    tag_title = serializers.CharField(source='tag_id.title', read_only=True)
    
    class Meta:
        model = TagBlog
        fields = ['tag_id', 'blog_id', 'tag_title']