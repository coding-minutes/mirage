from django.db import models
from mirage.config import Config


class Links(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    longUrl = models.URLField(max_length=256)
    author = models.UUIDField()

    def __str__(self):
        return self.code

def get_deleted_link():
    return Links.objects.get(code='deleted')

class Logs(models.Model):
    user = models.UUIDField()
    link = models.OneToOneField(Links, on_delete=models.SET(get_deleted_link))
    description = models.CharField(max_length=300)
