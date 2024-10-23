from email.mime import image
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    # image = models.ImageField(
    #     upload_to="item_images", default="item_images/default.jpg"
    # )
    # image = models.CharField(max_length=500, default="item_images/default.jpg")
    image = models.CharField(
        max_length=500,
        default="https://www.svgrepo.com/show/7059/plate-fork-and-knife.svg",
    )

    def __str__(self):
        return self.name
