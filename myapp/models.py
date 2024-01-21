from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length = 255)
    url = models.URLField(null = True)

    def __str__(self) -> str:
        return self.name

class Mymedia(models.Model):
    media_name = models.CharField(max_length = 255)
    url = models.URLField()

class Message(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField()
    text = models.TextField()
    sent_time = models.DateTimeField(auto_now_add = True)

class Token(models.Model):
    token = models.CharField(max_length = 32)
    is_active = models.BooleanField(default = True)