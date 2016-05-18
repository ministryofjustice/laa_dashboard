from django.utils import timezone
from django.db import models

class Service(models.Model):

    STATUS_COLOURS = (
    ('red', 'Red'),
    ('amber', 'Amber'),
    ('green', 'Green'),
    )

    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200, default='')
    url = models.CharField(max_length=200)
    enabled = models.BooleanField(default=True)
    auto_status = models.CharField(max_length=10, choices=STATUS_COLOURS, default='green')
    manual_status = models.CharField(max_length=10, choices=STATUS_COLOURS, default='green')
    last_status_code = models.IntegerField(default=0)
    last_check_time = models.DateTimeField(default=timezone.now)
    notes = models.TextField(default='', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'service_status'
