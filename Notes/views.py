from urllib import request
from warnings import filters

from django.shortcuts import render
from Notes.notesapi.permissions import LikePermission, NoteCreatePermission, NoteModify
from Notes.notesapi.throttling import NoteUploadThrottle
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Note
from Notes.notesapi.serializers import NotesSerializer
from rest_framework import filters

class NotesViewSet(generics.ListCreateAPIView):
    throttle_classes = [NoteUploadThrottle]
    permission_classes = [NoteCreatePermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'subject','grade']
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

    
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [NoteModify]

class NotesLikeViewSet(APIView):
    permission_classes = [LikePermission]
    def post(self, request, pk):
        note = Note.objects.get(pk=pk)
        note.liked_by.add(request.user)
        note.save()
        return Response({"message": "Note liked successfully."})
    def delete(self, request, pk):
        note = Note.objects.get(pk=pk)
        note.liked_by.remove(request.user)
        note.save()
        return Response({"message": "Note unliked successfully."})