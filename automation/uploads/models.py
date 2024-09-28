from django.db import models


class Upload(models.Model):
    # only the file paths are stored in the database, the actual files are stored in the designated folder (in this case: uploads/)
    file = models.FileField(upload_to="uploads/")
    model_name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name
