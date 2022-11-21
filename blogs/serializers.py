from rest_framework import serializers
from .models import Blog
from users.models import NewUser

from tagBlogs.serializers import TagBlogSerializer
from tagBlogs.serializers import CustomTagBlogSerializer
from comments.serializers import CommentSerializer

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'id', 'user']
        
class CustomBlogSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    tagblog_set = CustomTagBlogSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'id', 'user', 'tagblog_set']
        
class DetailedBlogSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    tagblog_set = CustomTagBlogSerializer(many=True, read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'id', 'user', 'tagblog_set', 'comment_set']