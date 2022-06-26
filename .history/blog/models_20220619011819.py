from turtle import title
from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(model.Model):
    author: models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title: models.CharField(max_length=200)
    text: models.TextField()
    createdDate: models.DateTimeField(default=timezone.now)
    publishedDate: models.DateTimeField(blank=True, null=True)