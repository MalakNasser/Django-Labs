from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="")
    rate = models.FloatField(default=0)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
