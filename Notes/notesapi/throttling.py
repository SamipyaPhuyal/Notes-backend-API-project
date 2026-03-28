from rest_framework import permissions
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle,BaseThrottle
from django.utils.timezone import now
from datetime import date
from Notes.models import Note

class NoteUploadThrottle(BaseThrottle):
    scope = 'note_uploads'
    def allow_request(self, request, view):
        if request.method == 'POST':
            today = date.today()
            user_notes_today = Note.objects.filter(uploaded_by=request.user,created_at__date=today).count()
            if user_notes_today == 5:
                return False
        return True