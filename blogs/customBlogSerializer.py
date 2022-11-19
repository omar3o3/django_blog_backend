from rest_framework import serializers
from .models import Blog
from users.models import NewUser
from tagBlogs.serializers import TagBlogSerializer
# from tags.serializers import TagListingField
from tags.serializers import TagSerializer

class CustomBlogSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    tagblog_set = TagBlogSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['title', 'content', 'id', 'user', 'tagblog_set']