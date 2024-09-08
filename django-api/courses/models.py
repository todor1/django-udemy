from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name
