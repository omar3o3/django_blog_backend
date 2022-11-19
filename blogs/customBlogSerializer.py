from rest_framework import serializers
from .models import Blog
from users.models import NewUser
from tagBlogs.serializers import TagBlogSerializer
# from tags.serializers import TagListingField
from tags.serializers import TagSerializer

class CustomBlogSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # user_owner = serializers.PrimaryKeyRelatedField(source='NewUser.id', read_only=True)
    # user_owner = serializers.PrimaryKeyRelatedField(source='NewUser', read_only=True)
    # user = serializers.PrimaryKeyRelatedField(queryset=NewUser.objects.all())
    # user = serializers.StringRelatedField(read_only=True)
    
    # !!!!! this is the one that will return the username for the owner of the post
    # !!!!! create custom serializer for fetching data in get requests?
    # user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    # tag = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')
    # tagblog_set = serializers.StringRelatedField(many=True)
    tagblog_set = TagBlogSerializer(many=True, read_only=True)
    # title = serializers.SlugRelatedField(read_only=True, slug_field='title')
    # tag_title = serializers.CharField(source='user.name', read_only=True)

    class Meta:
        model = Blog
        # fields = ['title', 'content', 'id', 'user', '']
        # fields = "__all__"
        fields = ['title', 'content', 'id', 'user', 'tagblog_set']