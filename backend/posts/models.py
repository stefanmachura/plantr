from django.db import models

from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    suspended = models.BooleanField(default=False)

    def suspend(self):
        self.suspended = True
        self.save()
