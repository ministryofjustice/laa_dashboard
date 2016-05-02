from __future__ import absolute_import
import sys
from datetime import datetime
from django.utils import timezone

from laa_dashboard.celery import app

from celery import shared_task
from .models import Service
import requests

from celery import task


def set_auto_status(status_code):
    ok_status_codes = [302, 200]

    if status_code in ok_status_codes:
        auto_status = True
    else:
        auto_status = False

    return auto_status


# @shared_task
# @app.task
# def auto_check():
#
#     sys.stdout = open('std_log.txt', 'w')
#     sys.sterr = open('std_err.txt', 'w')
#
#     print('***************auto_check**************')
#     services = Service.objects.order_by('name')
#
#     for service in services:
#
#         try:
#             print('Getting ' + service.url)
#             r = requests.get(service.url, verify=False, timeout=5)
#         except Exception as e:
#             print('**********Requests Error *******************:  ', e)
#
#         if r.status_code:
#             service.last_status_code = r.status_code
#             service.last_check_time = datetime.now()
#             service.auto_status = set_auto_status(r.status_code)
#         else:
#             service.last_status_code = 0
#             service.last_check_time = timezone.now()
#
#         service.save()

@app.task
def tta():
    file = open('celery_test.txt', 'w')
    file.write('Test')
    file.close()

    file = open('/Users/jamesnarey/celery_test.txt', 'w')
    file.write('Test')
    file.close()


@task
def ttb():
    print('Test')
