from django.db import models
from django.contrib.auth.models import User
import hashlib

class Link(models.Model):
    users = models.ManyToManyField(User)
    original_link = models.TextField()
    hashed_url = models.SlugField(max_length=32, blank=True)

    def save(self, *args, **kwargs):
        bytes_url = bytes(self.original_link, 'utf-8')
        self.hashed_url = hashlib.md5(bytes_url).hexdigest()
        super().save(*args, **kwargs)
