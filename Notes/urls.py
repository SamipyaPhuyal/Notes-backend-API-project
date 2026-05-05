from django.contrib import admin
from django.urls import path
from Notes.views import NotesViewSet, NoteDetailView, NotesLikeViewSet
from Notes.views import BookmarkViewSet
urlpatterns = [
    path("list/",NotesViewSet.as_view(),name="notes-list-create"),
    path("detail/<int:pk>/",NoteDetailView.as_view(),name="notes-detail"),
    path("detail/<int:pk>/like/",NotesLikeViewSet.as_view(),name="notes-like"),
    path("detail/<int:pk>/bookmark/",BookmarkViewSet.as_view(),name="notes-bookmark"),
]