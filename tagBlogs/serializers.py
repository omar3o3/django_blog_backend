from rest_framework import serializers
from .models import TagBlog
# from users.models import NewUser
from tags.serializers import TagSerializer
from tags.models import Tag

class TagBlogSerializer(serializers.ModelSerializer):
    
    # tag_title = serializers.SlugRelatedField(read_only=True, slug_field='title', queryset=Tag.objects.all())
    # tag_title = serializers.SlugRelatedField(read_only=True, slug_field='tag_id')
    # tags = TagSerializer(read_only=True)
    # tags = TagBlogSerializer(read_only=True, many=True, source="tagblog_set")
    # title = TagSerializer(read_only=True, many=True)
    tag_title = serializers.CharField(source='tag_id.title', read_only=True)
    
    class Meta:
        model = TagBlog
        # fields = ['title', 'content', 'id', 'user']
        # fields = "__all__"
        # fields = ['tag_id', 'blog_id']
        # fields = ['tag_id', 'blog_id', 'tag_title']
        fields = ['tag_id', 'blog_id', 'tag_title']