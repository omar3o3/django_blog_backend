from rest_framework import serializers
from .models import Blog
from users.models import NewUser

from tagBlogs.serializers import TagBlogSerializer
from tagBlogs.serializers import CustomTagBlogSerializer

class BlogSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    # tagblog_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'id', 'user']
        # fields = ['title', 'content', 'id', 'user', 'tagblog_set']
        
        
class CustomBlogSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    tagblog_set = CustomTagBlogSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'id', 'user', 'tagblog_set']