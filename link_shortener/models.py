from django.db import models
from django.contrib.auth.models import User



class Link(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    original_link = models.TextField()
    hashed_url = models.SlugField(max_length=32, blank=True)

    def save(self, *args, **kwargs):

        from .utils import get_url # из-за цикличного импорта

        if self.hashed_url is None or self.hashed_url == '':
            self.hashed_url = get_url()
        super().save(*args, **kwargs)
