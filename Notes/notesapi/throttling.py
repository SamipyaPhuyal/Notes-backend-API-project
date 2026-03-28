from rest_framework.throttling import UserRateThrottle,AnonRateThrottle

class NoteUploadThrottle(UserRateThrottle):
    scope = 'note_uploads'