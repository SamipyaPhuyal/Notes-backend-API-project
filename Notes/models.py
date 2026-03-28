from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    url=models.URLField(blank=True, null=True)
    subject=models.CharField(max_length=100)
    grade=models.CharField(max_length=100)
    liked_by=models.ManyToManyField(User, related_name='liked_notes', blank=True)
    uploaded_by=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
