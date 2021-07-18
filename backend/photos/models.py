from re import T
from django.db import models
from django.db.models.deletion import CASCADE

from posts.models import Post


class Photo(models.Model):
    alt_text = models.CharField(max_length=1000)
    published_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    temp_file = models.FileField(upload_to="uploads/", null=True)
    s3_url = models.CharField(max_length=256)
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name="photos", null=True)
