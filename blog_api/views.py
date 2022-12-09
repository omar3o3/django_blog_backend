from ast import Pass
from django.shortcuts import render

from blogs.models import Blog
from blogs.serializers import BlogSerializer
from blogs.serializers import CustomBlogSerializer
from blogs.serializers import DetailedBlogSerializer

from blogs.models import UserFollowing
from blogs.serializers import UserFollowingSerializer

from comments.serializers import CommentSerializer
from comments.serializers import CustomCommentSerializer

from tags.models import Tag
from tags.serializers import TagSerializer

from tagBlogs.models import TagBlog
from tagBlogs.serializers import TagBlogSerializer


from comments.models import Comment

from users.models import NewUser
from users.serializers import UserSerializer
from users.serializers import CustomUserSerializer

from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes

from rest_framework import status, viewsets, filters, generics
# permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_run(request):
    return Response('hi there')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_blogs(request):
    # all_blogs = Blog.objects.all()
    all_blogs = Blog.objects.order_by('-created_at')
    blog_serializer = CustomBlogSerializer(all_blogs, many = True)
    return Response(blog_serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):    
    blog_data = request.data['blog_data']
    tag_data = request.data['tag_data']
    
    blog_serializer = BlogSerializer(data=blog_data)
    if blog_serializer.is_valid():
        blog_post = blog_serializer.save()
        # print(tag_data)
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
@permission_classes([IsAuthenticated])
def create_comment(request):
    comment_serializer = CommentSerializer(data=request.data)
    if comment_serializer.is_valid():
        # pass
        # print(comment_serializer)
        comment_post = comment_serializer.save()
        comment_data = comment_serializer.data
        # print(request.data)
        comment_data['user'] = NewUser.objects.get(pk=request.data['user']).user_name
        return Response(comment_data, status=status.HTTP_201_CREATED)
    return Response(comment_serializer.erros, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detailed_blog_view(request, blogId):
    requested_blog = Blog.objects.get(pk=blogId)
    detailed_blog = DetailedBlogSerializer(requested_blog)
    if detailed_blog:
        return Response(detailed_blog.data, status=status.HTTP_200_OK)
    return Response(detailed_blog.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search_blog_user(request):
    requested_user = request.data['searchContent']
    found_user = NewUser.objects.get(user_name=requested_user)
    if found_user:
        bl = Blog.objects.filter(user = found_user).order_by('-created_at')
        bl_data = CustomBlogSerializer(bl, many=True)
        return Response(bl_data.data, status=status.HTTP_200_OK)
    return Response({"message": 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search_blog_tag(request):
    requested_tags = request.data['searchContent']
    tag_list = requested_tags.split()
    found_blogs = Blog.objects.filter(tagblog__tag_id__title__in = tag_list).order_by('-created_at')
    if found_blogs:
        bl_data = CustomBlogSerializer(found_blogs, many=True)
        return Response(bl_data.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'tag(s) not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search_blog_content(request):
    requested_content = request.data['searchContent']
    found_blogs = Blog.objects.filter(content__contains = requested_content).order_by('-created_at')
    if found_blogs:
        bl_data = CustomBlogSerializer(found_blogs, many=True)
        return Response(bl_data.data, status=status.HTTP_200_OK)
    return Response({'message': 'no blog with that content found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_history(request, userId):
    all_blogs = Blog.objects.filter(user = userId).order_by('-created_at')
    blog_serializer = CustomBlogSerializer(all_blogs, many = True)
    if all_blogs:
        return Response(blog_serializer.data, status=status.HTTP_200_OK)
    return Response({'message': 'user has not posted any content'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def account_info(request , userId):
    user = NewUser.objects.get(pk=userId)
    # user_serializer = UserSerializer(user)
    user_serializer = CustomUserSerializer(user)
    if user:
        return Response(user_serializer.data, status=status.HTTP_200_OK)
    return Response({'message': 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def patch_user(request, userId):
    pass
    # serializer = CommentSerializer(comment, data=request.data, partial=True)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_following(request):
    user_following_serializer = UserFollowingSerializer(data=request.data)
    if user_following_serializer.is_valid():
        user_following = user_following_serializer.save()
        return Response(user_following_serializer.data, status=status.HTTP_200_OK)
    return Response({'message': 'could not create following association'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_following(request):
    current_user = request.data.logged_in_user_name
    target_user = request.data.target_user_name
    following_association = UserFollowing.objects.get(user_id__user_name = current_user, following_user_id__user_name=target_user)
    following_association.delete()

    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_following_posts(request, userId):
    user = NewUser.objects.get(pk=userId)
    user_following = user.following.all()
    users_being_followed = NewUser.objects.filter(followers__in=user_following)
    found_blogs = Blog.objects.filter(user__in=users_being_followed).order_by('-created_at')
    if found_blogs:
        blog_serializer = CustomBlogSerializer(found_blogs, many = True)
        return Response(blog_serializer.data, status=status.HTTP_200_OK)
    return Response({'message': 'user does not follow any users or those users have not posted anything'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def view_other_user_history(request, user_name):
    all_blogs = Blog.objects.filter(user__user_name = user_name).order_by('-created_at')
    if all_blogs.exists():
        blog_serializer = CustomBlogSerializer(all_blogs , many = True)
        return Response(blog_serializer.data, status=status.HTTP_200_OK)
    return Response({'message': 'user has not posted anything'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def view_other_account_info(request , user_name , loggedInUserId):
    user = NewUser.objects.get(user_name=user_name)
    # user_serializer = UserSerializer(user)
    user_serializer = CustomUserSerializer(user)
    if user:
        user_data = user_serializer.data
        user_followers = user.followers.all()
        logged_in_user_follows_requested_user = user_followers.filter(user_id = loggedInUserId).exists()
        user_data['followed_by_user'] = logged_in_user_follows_requested_user
        return Response(user_data, status=status.HTTP_200_OK)
    return Response({'message': 'user does not exist'}, status=status.HTTP_404_NOT_FOUND)
    