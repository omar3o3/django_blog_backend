from django.urls import path

from . import views

urlpatterns = [
    path('reddit-scrap', views.reddit_scrap),
    path('twitter-scrap', views.twitter_scrap),
]