from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Service
import requests

# Create your views here.

ok_status_codes = [302, 200]


def main_page(request):

    services = Service.objects.order_by('name')

    statuses = {}

    for service in services:
        if service.name != 'Portal':
            try:
                r = requests.get(service.url, verify=False, timeout=5)
            except:
                print(service.url)

            if r.status_code in ok_status_codes:
                statuses[service.name] = 'Up'
            else:
                statuses[service.name] = 'Down'



    template = loader.get_template('service_status/ITSystemsStatuses.html')

    context = RequestContext(request, {'statuses': statuses, })

    return HttpResponse(template.render(context))

    #return HttpResponse(str(statuses))

    #response = render(request, 'service_status/ITSystemsStatuses.html')

    #return response
