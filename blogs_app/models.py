from django.db import models

class post(models.Model):
    title = models.CharField()
    category = models.CharField()
    content = models.TextField()
    date = models.DateTimeField()
