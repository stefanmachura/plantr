from django.db import models

class Photo(models.Model):
    alt_text = models.CharField(max_length=1000)
    published_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    temp_file = models.FileField(upload_to="uploads/")
    s3_url = models.CharField(max_length=256)