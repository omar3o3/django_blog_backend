from rest_framework import serializers
from .models import Comment
from users.models import NewUser

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'content', 'blog']
        
        
class CustomCommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    class Meta:
        model = Comment
        fields = ['user', 'content', 'blog']