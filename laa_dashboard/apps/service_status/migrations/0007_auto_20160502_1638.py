# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 16:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service_status', '0006_auto_20160502_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='last_check_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]