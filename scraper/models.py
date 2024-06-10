from django.db import models

# Create your models here.
import uuid
class Job(models.Model):
    job_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Task(models.Model):
    job = models.ForeignKey(Job, related_name='tasks', on_delete=models.CASCADE)
    coin = models.CharField(max_length=10)
    output = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=20, default='PENDING')