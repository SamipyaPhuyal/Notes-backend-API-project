from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from django.contrib.auth.models import User
from Users.Usersapi.serializers import RegistrationSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from Users.Usersapi.permissions import LogoutPermission, UserModify
# Create your views here.
class UserViewSet(APIView):
    permission_classes = [UserModify]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data["password"] != serializer.validated_data["password2"]:
                return Response({"error": "Passwords do not match"}, status=400)
            if User.objects.filter(username=serializer.validated_data["username"]).exists():
                return Response({"error": "Username already exists"}, status=400)
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class LogoutView(APIView):
    permission_classes = [LogoutPermission]
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Logged out successfully."})