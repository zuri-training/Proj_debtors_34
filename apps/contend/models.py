from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Room(models.Model):
    room_name = models.CharField(max_length=1000)


class Message(models.Model):
    value = models.CharField(max_length=100000000, default="default")
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=1000, default="default")
    room = models.CharField(max_length=10000000, default="default")