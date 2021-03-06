from __future__ import absolute_import
from datetime import datetime
from django.utils import timezone

from laa_dashboard.celery import app

from .models import Service
import requests

# Consider using the lines below to import auto_check.py
# and assign auto_check to a new, decorated variable, i.e.
#
# @app.task
# decorated_auto_check = tasks.auto_check
#
# from pathlib import Path
# p = Path(__file__).parents[3]


def get_status_colour(status_code):
    green_status_codes = [302, 200]
    amber_status_codes = []
    red_status_codes = []

    if status_code in green_status_codes:
        auto_status = 'green'
    elif status_code in amber_status_codes:
        auto_status = 'amber'
    else:
        auto_status = 'red'

    return auto_status


@app.task
def auto_check():

    print('***************auto_check**************')
    services = Service.objects.order_by('name')

    for service in services:

        try:
            print('Getting ' + service.url)
            r = requests.get(service.url, verify=False, timeout=5)
        except Exception as e:
            print('**********Requests Error *******************:  ', e)

        if r.status_code:
            service.last_status_code = r.status_code
            service.last_check_time = datetime.now()
            service.auto_status = get_status_colour(r.status_code)
        else:
            service.last_status_code = 0
            service.last_check_time = timezone.now()

        service.save()

