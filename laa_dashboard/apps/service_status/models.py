from django.db import models


class Service(models.Model):

    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    enabled = models.BooleanField(default=True)
    auto_status = models.BooleanField(default=False)
    manual_status = models.BooleanField(default=False)
    notes = models.TextField(default='')

    def __str__(self):
        return self.name

