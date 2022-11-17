from rest_framework import serializers
from .models import Blog
from users.models import NewUser

class BlogSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(read_only=True)
    # user_owner = serializers.PrimaryKeyRelatedField(source='NewUser.id', read_only=True)
    # user_owner = serializers.PrimaryKeyRelatedField(source='NewUser', read_only=True)
    # user = serializers.PrimaryKeyRelatedField(queryset=NewUser.objects.all())
    # user = serializers.StringRelatedField(read_only=True)
    
    # !!!!! this is the one that will return the username for the owner of the post
    # !!!!! create custom serializer for fetching data in get requests?
    # user = serializers.SlugRelatedField(read_only=True, slug_field='user_name')

    class Meta:
        model = Blog
        # fields = ['title', 'content', 'id', 'user', 'tagblog_set', 'tag_set']
        fields = "__all__"