from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateTimeField()
    genre = models.CharField(default="r&b", max_length=50)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.post