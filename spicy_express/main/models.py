# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(default='example@example.com')
    message = models.TextField()
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    
    
class Question(models.Model):
    user_name = models.CharField(max_length=100)
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question by {self.user_name} on {self.created_at}"


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)