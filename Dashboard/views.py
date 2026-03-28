from django.shortcuts import render
from Notes.models import Note
from rest_framework.views import APIView
from rest_framework.response import Response
from .dashboard_api.serializers import DashboardSerializer
from rest_framework import serializers
# Create your views here.
class DashboardSerializerView(APIView):
    def get(self, request):
        serializer = DashboardSerializer(instance={})
        return Response(serializer.data)