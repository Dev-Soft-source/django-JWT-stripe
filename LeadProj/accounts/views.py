# accounts/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsAdmin, IsCustomer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Hello Admin!"})

class CustomerOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsCustomer]
    
    def get(self, request):
        return Response({"message": "Hello Customer!"})

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):        
        return Response({'message': f'Hello, {request.user.email}!'})
