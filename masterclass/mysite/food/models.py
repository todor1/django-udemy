from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(
        max_length=500,
        default="https://www.svgrepo.com/show/7059/plate-fork-and-knife.svg",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
