from rest_framework import serializers
from .models import Blog
from .models import UserFollowing
from users.models import NewUser

from tagBlogs.serializers import TagBlogSerializer
from tagBlogs.serializers import CustomTagBlogSerializer
from comments.serializers import CommentSerializer
from comments.serializers import CustomCommentSerializer

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'id', 'user']
        
class CustomBlogSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    tagblog_set = CustomTagBlogSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        # fields = ['title', 'content', 'id', 'user', 'tagblog_set']
        fields = ['title', 'content', 'id', 'user', 'tagblog_set', 'nyc_time']
        
class DetailedBlogSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    tagblog_set = CustomTagBlogSerializer(many=True, read_only=True)
    # comment_set = CommentSerializer(many=True, read_only=True)
    comment_set = CustomCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        # fields = ['title', 'content', 'id', 'user', 'tagblog_set', 'comment_set']
        fields = ['title', 'content', 'id', 'user', 'tagblog_set', 'comment_set', 'nyc_time']
        

class UserFollowingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserFollowing
        fields = ['user_id' , 'following_user_id']