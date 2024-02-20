from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    created_at = models.DateTimeField(auto_now_add=True)

class NoteHistory(models.Model):
    note = models.ForeignKey(Note, related_name='versions', on_delete=models.CASCADE)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
