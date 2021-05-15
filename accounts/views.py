from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import UserRegisterSerializer

# Create your views here.

class RegisterAPIView(APIView):
    
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            response_data = {
                'refresh_token':str(refresh),
                'access_token':str(refresh.access_token),
                'user': serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogOutAPIView(APIView):
    
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token_obj = RefreshToken(refresh_token)
            token_obj.blacklist()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

