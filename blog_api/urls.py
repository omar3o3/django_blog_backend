from django.urls import path

from . import views

urlpatterns = [
    path('create-post', views.create_post),
    path('test-run', views.test_run),
    path('get-blogs', views.get_blogs),
    path('create-comment', views.create_comment),
    path('detailedBlogView/<int:blogId>', views.detailed_blog_view),
    path('search-user', views.search_blog_user),
    path('search-tag', views.search_blog_tag),
    path('search-blog-content', views.search_blog_content),
    path('user-history/<int:userId>', views.user_history),
    path('account-info/<int:userId>', views.account_info),
    path('patch-user/<int:userId>', views.patch_user),
]