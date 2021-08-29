from django.db import models
from mirage.config import Config


class Links(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    longUrl = models.URLField(max_length=256)
    author = models.UUIDField()
