from django.urls import path

from . import views

urlpatterns = [
    path('create-post', views.create_post),
    path('test-run', views.test_run),
    path('get-blogs', views.get_blogs),
    path('create-comment', views.create_comment),
    path('detailedBlogView/<int:blogId>', views.detailed_blog_view)
]