from rest_framework import serializers
from .models import Blog
from users.models import NewUser

class BlogSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    tagblog_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Blog
        
        fields = ['title', 'content', 'id', 'user', 'tagblog_set']