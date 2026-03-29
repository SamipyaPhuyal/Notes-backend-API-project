
import Notes
from Notes.models import Note
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Count

class UserSerializer(serializers.ModelSerializer):
    upload_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["id", "username","upload_count"]
    def get_upload_count(self, obj):
        return Note.objects.filter(uploaded_by=obj).count()
    
class UserProfileSerializer(serializers.ModelSerializer):
    liked_notes = serializers.SerializerMethodField()
    uploaded_notes = serializers.SerializerMethodField()
    upload_count = serializers.SerializerMethodField()
    likes_received = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["id", "username", "liked_notes", "uploaded_notes", "upload_count", "likes_received"]
    def get_upload_count(self, obj):
        return Note.objects.filter(uploaded_by=obj).count()
    def get_liked_notes(self, obj):
        return Note.objects.filter(liked_by=obj).count()
    def get_uploaded_notes(self, obj):
        return Note.objects.filter(uploaded_by=obj).values_list("title",flat=True)
    def get_likes_received(self, obj):
        return (
            Note.objects
            .filter(uploaded_by=obj)
            .aggregate(total_likes=Count('liked_by'))['total_likes']
            or 0
    )

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "password", "password2"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data.get("email")
        )
        return user
    
        