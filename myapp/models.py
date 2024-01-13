from django.db import models

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