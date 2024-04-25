from django.db import models
from user_app.models import user


class post(models.Model):
    title = models.CharField(max_length = 50)
    category = models.CharField(max_length = 15)
    content = models.TextField()
    date = models.DateTimeField()
    written_by = models.CharField(max_length = 50, default='default user')
    writer = models.ForeignKey(user, on_delete=models.PROTECT, default='defaultUser')