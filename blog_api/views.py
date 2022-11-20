from django.shortcuts import render

from blogs.models import Blog
from blogs.serializers import BlogSerializer

from blogs.serializers import CustomBlogSerializer

from comments.serializers import CommentSerializer

from tags.models import Tag
from tags.serializers import TagSerializer

from tagBlogs.models import TagBlog
from tagBlogs.serializers import TagBlogSerializer


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

@api_view(['GET'])
def get_blogs(request):
    permission_classes = [IsAuthenticated]
    all_blogs = Blog.objects.all()
    
    blog_serializer = CustomBlogSerializer(all_blogs, many = True)
    return Response(blog_serializer.data)


@api_view(['POST'])
def create_post(request):    
    permission_classes = [IsAuthenticated]
    blog_data = request.data['blog_data']
    tag_data = request.data['tag_data']
    
    blog_serializer = BlogSerializer(data=blog_data)
    if blog_serializer.is_valid():
        blog_post = blog_serializer.save()
        print(tag_data)
        for x in tag_data['tags']:
            tag_serializer = TagSerializer(data={'title': x})
            if tag_serializer.is_valid():
                tag_post = tag_serializer.save()
                tagblog_serializer1 = TagBlogSerializer(data={'tag_id': tag_post.id, 'blog_id': blog_post.id})
                if tagblog_serializer1.is_valid():
                    tagblog_post = tagblog_serializer1.save()
                    if blog_post and tag_post and tagblog_post:
                        json1 = [blog_serializer.data , tagblog_serializer1.data]
            else:
                existing_tag = Tag.objects.get(title=x)
                tagblog_serializer2 = TagBlogSerializer(data={'tag_id': existing_tag.id, 'blog_id': blog_post.id})
                if tagblog_serializer2.is_valid():
                    tagblog_post2 = tagblog_serializer2.save()
                    if blog_post and tagblog_post2:
                        json2 = [blog_serializer.data , tagblog_serializer2.data]
        return Response(status=status.HTTP_201_CREATED)
    return Response(blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_comment(request):
    # print('----------------------------------------------')
    # print(request.data)
    # print('----------------------------------------------')
    comment_serializer = CommentSerializer(data=request.data)
    if comment_serializer.is_valid():
        pass
        # print(comment_serializer)
        comment_post = comment_serializer.save()
        return Response(comment_serializer.data, status=status.HTTP_201_CREATED)
    return Response(comment_serializer.erros, status==status.HTTP_400_BAD_REQUEST)
    
