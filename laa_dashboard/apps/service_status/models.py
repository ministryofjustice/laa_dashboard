from django.db import models


class Service(models.Model):

    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    enabled = models.BooleanField(default=True)

    def __str__(self):
        return self.name

