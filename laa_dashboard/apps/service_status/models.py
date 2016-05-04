from django.utils import timezone
from django.db import models



class Service(models.Model):

    STATUS_COLOURS = (
    ('red', 'Red'),
    ('amber', 'Amber'),
    ('green', 'Green'),
    )

    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    enabled = models.BooleanField(default=True)
    auto_status = models.CharField(max_length=10, choices=STATUS_COLOURS, blank=True)
    manual_status = models.CharField(max_length=10, choices=STATUS_COLOURS, blank=True)
    last_status_code = models.IntegerField(default=0)
    last_check_time = models.DateTimeField(default=timezone.now)
    notes = models.TextField(default='')

    def __str__(self):
        return self.name

