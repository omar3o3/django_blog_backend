from rest_framework import serializers
from .models import Tag
# from users.models import NewUser

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title']
    