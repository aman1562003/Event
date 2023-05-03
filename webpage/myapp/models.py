from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    is_liked = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.event_name}"