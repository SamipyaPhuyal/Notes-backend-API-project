from rest_framework import permissions
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle,ScopedRateThrottle
from django.utils.timezone import now
from datetime import date
from Notes.models import Note

# class NoteUploadThrottle(ScopedRateThrottle):
    # scope = 'note_uploads'
    # if request.user.is_authenticated and request.method == 'POST':
    #     today = date.today()
    #     upload_count = Note.objects.filter(uploaded_by=request.user, uploaded_at__date=today).count()
    #     if upload_count >= 5:
    #         return True