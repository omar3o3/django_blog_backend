from django.urls import path

from . import views
from .views import BlacklistTokenUpdateView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('create_user', views.create_user),
    path('test_run', views.test_run),
    path('get_users', views.get_users),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(), name='blacklist')
    # path('logout/blacklist/', blacklistTokenUpdateView.as_view(), name='blacklist')
]