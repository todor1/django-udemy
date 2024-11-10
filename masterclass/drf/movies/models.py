from email.mime import image
from django.db import models


# Create your models here.
class MovieData(models.Model):
    name = models.CharField(max_length=100)
    duration = models.FloatField()
    rating = models.FloatField()
    year = models.IntegerField()
    genre = models.CharField(max_length=100, default="action")
    image = models.ImageField(upload_to="images/", default="images/none/default.jpg")

    def __str__(self):
        return self.name
