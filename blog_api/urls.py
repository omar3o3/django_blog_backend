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
    path('get-following-posts/<int:userId>', views.get_following_posts),
    path('create-following', views.create_following),
    # path('delete-following', views.delete_following),
    path('delete-following/<str:logged_in_user_name>/<str:target_user_name>', views.delete_following),
    path('view-other-user-history/<str:user_name>', views.view_other_user_history),
    path('view-other-account-info/<str:user_name>/<int:loggedInUserId>', views.view_other_account_info),
]