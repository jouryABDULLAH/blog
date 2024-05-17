from django.db import models
from user_app.models import user

class post(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=15)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created
    written_by = models.ForeignKey(user, on_delete=models.PROTECT, to_field='username')

    def __str__(self):
        return self.title
