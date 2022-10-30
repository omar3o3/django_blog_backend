from rest_framework import serializers
from .models import NewUser
import pdb

class UserSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = NewUser
        fields = ('email', 'user_name', 'first_name', 'last_name','password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
            
    