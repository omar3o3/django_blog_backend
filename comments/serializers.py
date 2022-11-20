from rest_framework import serializers
from .models import Comment
from users.models import NewUser

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'content', 'blog']