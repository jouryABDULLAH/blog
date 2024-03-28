from django.db import models

class post(models.Model):
    title = models.CharField(max_length = 50)
    category = models.CharField(max_length = 15)
    content = models.TextField()
    date = models.DateTimeField()
    written_by = models.CharField(max_length = 50, default='default user')
