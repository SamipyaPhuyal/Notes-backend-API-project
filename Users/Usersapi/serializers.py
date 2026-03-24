
from Notes.models import Note
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    upload_count = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["id", "username","upload_count"]
    def get_upload_count(self, obj):
        return Note.objects.filter(uploaded_by=obj).count()
        
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
    
        