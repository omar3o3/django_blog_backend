from django.urls import path

from . import views

urlpatterns = [
    path('reddit-scrap', views.reddit_scrap),
]