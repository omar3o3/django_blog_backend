from django.urls import path

from . import views

urlpatterns = [
    path('create_user', views.create_user),
    path('test_run', views.test_run),
    path('get_users', views.get_users)
]