from django.db import models


class UploadedImage(models.Model):
    file = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
