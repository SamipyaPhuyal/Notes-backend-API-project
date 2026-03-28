
from webbrowser import get

from Notes.models import Note
from rest_framework import serializers 
class NotesSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.StringRelatedField(source="uploaded_by.username")
    url=serializers.HyperlinkedIdentityField(view_name="notes-detail")
    liked_by=serializers.SerializerMethodField()
    def get_liked_by(self, obj):
        return [user.username for user in obj.liked_by.all()]
    class Meta:
        model = Note
        read_only_fields = ["uploaded_by","url"]
        exclude = ["created_at","updated_at"]
    
class NotesDetailSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.StringRelatedField(source="uploaded_by.username")
    liked_by=serializers.SerializerMethodField()
    class Meta:
        model = Note
        read_only_fields = ["uploaded_by","url"]
        exclude= ["url"]
        
    get_liked_by = serializers.SerializerMethodField()
    def get_liked_by(self, obj):
        return [user.username for user in obj.liked_by.all()]