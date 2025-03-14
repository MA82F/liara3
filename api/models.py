from django.db import models

class History(models.Model):
    expression = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
