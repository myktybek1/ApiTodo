from django.db import models

class Posts(models.Model):
    plan = models.CharField(max_length=250)
    completed = models.BooleanField(default=False, blank=True, null=True)