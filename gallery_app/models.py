from django.contrib.auth.models import User
from django.db import models


class Voice(models.Model):
    file_name = models.CharField(max_length=256, unique=True, null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    voice_file = models.FileField(upload_to='voices/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Image(models.Model):
    file_name = models.CharField(max_length=256, unique=True, null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Video(models.Model):
    file_name = models.CharField(max_length=256, unique=True, null=True, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
