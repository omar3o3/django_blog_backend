from rest_framework import serializers
from .models import TagBlog
# from users.models import NewUser

class TagBlogSerializer(serializers.ModelSerializer):
    
    # tag_title = serializers.SlugRelatedField(read_only=True, slug_field='tag_id')
    # tag_title = serializers.SlugRelatedField(read_only=True, slug_field='tag_id')
    
    class Meta:
        model = TagBlog
        # fields = ['title', 'content', 'id', 'user']
        # fields = "__all__"
        # fields = ['tag_id', 'blog_id']
        fields = ['tag_id', 'blog_id']