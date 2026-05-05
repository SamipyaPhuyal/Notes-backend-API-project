from urllib import request
from warnings import filters
from django.shortcuts import render
from Notes.notesapi.permissions import BookmarkPermission, LikePermission, NoteCreatePermission, NoteModify
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

class BookmarkViewSet(APIView):
    permission_classes = [BookmarkPermission]
    def post(self, request,**kwargs):
        note = Note.objects.filter(pk=kwargs.get('pk')).first()
        if note is None:
            return Response({"error": "Note not found"}, status=404)
        bookmark= Bookmarks.objects.get_or_create(user=request.user, note=note)
        if bookmark[1]:
            return Response({"message": "Note bookmarked successfully."}, status=201)
        else:
            return Response({"message":"error"}, status=200)
    def delete(self, request,**kwargs):
        note = Note.objects.filter(pk=kwargs.get('pk')).first()
        if note is None:
            return Response({"error": "Note not found"}, status=404)
        bookmark = Bookmarks.objects.filter(user=request.user, note=note).first()
        if bookmark:
            bookmark.delete()
            return Response({"message": "Bookmark Removed successfully."}, status=200)
        else:
            return Response({"error": "Bookmark not found"}, status=404)