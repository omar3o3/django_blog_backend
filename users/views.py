# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import NewUser
from .serializers import UserSerializer
from rest_framework import status

from rest_framework.permissions import AllowAny

# Create your views here.
    
# @api_view(['POST'])
# def create_user(request):
#     rq = request.data
#     user = NewUser.objects.create(
#         user_name= rq['user_name'],
#         email = rq['email'],
#         first_name = rq['first_name'],
#         last_name = rq['last_name'],
#         )
#     user.set_password(rq['password'])
#     user.save()
#     serializer = UserSerializer(user)
#     return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    permission_classes = [AllowAny]
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            json = serializer.data
            return Response(json, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
@api_view(['GET'])
def get_users(request):
    all_users = NewUser.objects.all()
    serializer = UserSerializer(all_users, many = True)
    return Response(serializer.data)
    
    
@api_view(['GET'])
def test_run(request):
    return Response('hi there')