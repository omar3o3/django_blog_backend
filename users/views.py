# from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import NewUser
from .serializers import UserSerializer
from rest_framework import status

from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CustomObtainPairSerializer

from rest_framework.views import APIView

# Create your views here.

@api_view(['POST'])
def create_user(request):
    permission_classes = [AllowAny]
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            json = serializer.data
            json["user_id"] = user.id
            return Response(json, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
@api_view(['GET'])
def get_users(request):
    all_users = NewUser.objects.all()
    serializer = UserSerializer(all_users, many = True)
    return Response(serializer.data)


class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer


@api_view(['GET'])
def test_run(request):
    return Response('hi there')