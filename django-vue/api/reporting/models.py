from django.db import models

# Create your models here.


class Order(models.Model):
    # amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True)
