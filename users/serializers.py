from rest_framework import serializers
from .models import NewUser
import pdb

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # pdb.set_trace()
        model = NewUser
        fields = [
            'email',
            'user_name',
            'first_name',
            'last_name',
            'password'
        ]
        
        def create(self):
            print('from create inside serializer')
            
    