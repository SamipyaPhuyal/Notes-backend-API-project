from django.contrib import admin
from django.urls import path
from Notes.views import NotesViewSet
urlpatterns = [
    path("list/",NotesViewSet.as_view(),name="notes-list-create"),
    path("detail/<int:pk>/",NotesViewSet.as_view(),name="notes-detail"),
]