from django.db import models

class user(models.Model):
    username = models.CharField(max_length = 20, primary_key=True)
    