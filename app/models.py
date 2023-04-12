from django.conf import settings
from django.db import models

class Post(models.Model):
    contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_text = models.CharField(max_length=140, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

