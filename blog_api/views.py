from django.shortcuts import render

from blogs.models import Blog
from tags.models import Tag
from comments.models import Comment
from users.models import NewUser

from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status, viewsets, filters, generics
# permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

@api_view(['GET'])
def test_run(request):
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [IsAuthenticated]
    return Response('hi there')


@api_view(['POST'])
def create_post(request):
    pass