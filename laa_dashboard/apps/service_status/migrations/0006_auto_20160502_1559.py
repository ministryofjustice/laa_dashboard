# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 15:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service_status', '0005_service_auto_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='last_check_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='service',
            name='last_status_code',
            field=models.IntegerField(default=0),
        ),
    ]