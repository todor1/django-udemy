from unicodedata import category
from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    dicscount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.CharField(max_length=300)

    def __str__(self):
        return self.title
