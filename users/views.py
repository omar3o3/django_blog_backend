# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import NewUser
from .serializers import UserSerializer
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    
@api_view(['GET'])
def get_users(request):
    all_users = NewUser.objects.all()
    serializer = UserSerializer(all_users, many = True)
    return Response(serializer.data)
    
    
@api_view(['GET'])
def test_run(request):
    return Response('hi there')