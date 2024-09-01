from django.db import models

# Create your models here.


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.item
        # return self.item + " | " + str(self.completed)
