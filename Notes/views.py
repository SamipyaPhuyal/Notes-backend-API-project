from urllib import request

from django.shortcuts import render
from Notes.notesapi.permissions import NoteModify
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .models import Note
from Notes.notesapi.serializers import NotesSerializer

class NotesViewSet(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
        self.request.user.uploads += 1
        self.request.user.save()
        
    
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [NoteModify]
    
class NotesLikeViewSet(APIView):
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