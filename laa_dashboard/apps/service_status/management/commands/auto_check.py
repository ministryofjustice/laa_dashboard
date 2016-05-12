#!/usr/bin/env python
# from __future__ import absolute_import
# import os
import requests

from datetime import datetime
from django.utils import timezone
from django.core.management.base import BaseCommand

from service_status.models import Service


class Command(BaseCommand):

    def get_status_colour(self, status_code):
        green_status_codes = [302, 200]
        amber_status_codes = []
        #red_status_codes = []

        if status_code in green_status_codes:
            auto_status = 'green'
        elif status_code in amber_status_codes:
            auto_status = 'amber'
        else:
            auto_status = 'red'

        return auto_status

    def handle(self, *args, **kwargs):

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
                service.auto_status = self.get_status_colour(r.status_code)
            else:
                service.last_status_code = 0
                service.last_check_time = timezone.now()

            service.save()


# if __name__ == '__main__':
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', '..laa_dashboard.settings')
    # configure()
    # django.setup()

