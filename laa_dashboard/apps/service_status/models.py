from django.utils import timezone
from django.db import models



class Service(models.Model):

    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    enabled = models.BooleanField(default=True)
    auto_status = models.BooleanField(default=False)
    last_status_code = models.IntegerField(default=0)
    last_check_time = models.DateTimeField(default=timezone.now)
    manual_status = models.BooleanField(default=False)
    notes = models.TextField(default='')

    def __str__(self):
        return self.name

