from django.db import models
from django.utils.timezone import now

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateField(default=now)

    def __str__(self):
        return self.title
