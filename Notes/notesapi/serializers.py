
from Notes.models import Note
from rest_framework import serializers 
class NotesSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.StringRelatedField(source="uploaded_by.username")
    url=serializers.HyperlinkedIdentityField(view_name="notes-detail")
    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ["uploaded_by","url"]