from __future__ import absolute_import

# from laa_dashboard.celery import app

from celery import shared_task
from .models import Service
import requests

ok_status_codes = [302, 200]


@shared_task
def auto_check():

    print('***************auto_check**************')
    services = Service.objects.order_by('name')

    for service in services:

        try:
            print('Getting ' + service.url)
            r = requests.get(service.url, verify=False, timeout=5)
        except Exception as e:
            print('**********Requests Error *******************:  ', e)

        if r.status_code and r.status_code in ok_status_codes:
            service.auto_status = True
        else:
            service.auto_status = False

        service.save()

