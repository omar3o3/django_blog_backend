from rest_framework import serializers
from .models import NewUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = [
            'email',
            'user_name',
            'first_name',
            'last_name'
        ]
    