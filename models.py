from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, default='Medium')
    status = models.CharField(max_length=20, default='Pending')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title