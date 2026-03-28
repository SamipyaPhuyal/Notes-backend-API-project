from rest_framework import serializers
from Notes.models import Note
from django.db.models import Count
from django.contrib.auth.models import User

class DashboardSerializer(serializers.Serializer):
    total_users = serializers.IntegerField(read_only=True)
    total_notes = serializers.IntegerField(read_only=True)
    most_liked_note = serializers.CharField(read_only=True, default="None")
    most_active_user = serializers.CharField(read_only=True, default="None")
    trending_notes = serializers.CharField(read_only=True, default="None")

    def to_representation(self, instance=None):
        data = super().to_representation(instance)
        data['total_users'] = User.objects.count()
        data['total_notes'] = Note.objects.count()
        most_liked_note = Note.objects.annotate(like_count=Count('liked_by')).order_by('-like_count').first()
        data['most_liked_note'] = most_liked_note.title if most_liked_note else None
        most_active_user = User.objects.annotate(note_count=Count('note')).order_by('-note_count').first()
        data['most_active_user'] = User.objects.annotate(upload_count=Count('note')).order_by('-upload_count').first().username if most_active_user else None
        data['trending_notes'] = ", ".join(Note.objects.annotate(like_count=Count('liked_by')).order_by('-like_count')[:5].values_list('title', flat=True))
        return data