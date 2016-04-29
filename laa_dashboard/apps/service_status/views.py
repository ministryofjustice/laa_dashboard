import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
from .models import Service
import requests

# Create your views here.

ok_status_codes = [302, 200]


def main_page(request):

    print('main_page')
    print(str(request))

    services = Service.objects.order_by('name')

    statuses = {}

    for service in services:

        # try:
        #     r = requests.get(service.url, verify=False, timeout=5)
        # except:
        #     print(service.url)

        if True:
        #if r.status_code in ok_status_codes:
            statuses[service.name] = 'Up'
        else:
            statuses[service.name] = 'Down'

    template = loader.get_template('service_status/service_status.html')

    context = {'statuses': statuses, }

    # context = RequestContext(request, {'statuses': statuses, })
    #

    #
    return HttpResponse(template.render(context))


def ajax(request):

    print('ajax')
    print(str(request))

    services = Service.objects.order_by('name')

    statuses = {}

    for service in services:

        try:
            print('Getting ' + service.url)
            r = requests.get(service.url, verify=False, timeout=5)
        except:
            print(service.url)

        if r.status_code in ok_status_codes:
            statuses[service.name] = True
        else:
            statuses[service.name] = False

    #response = json.dumps(statuses)

    print('ajax')

    return JsonResponse(statuses)


# def test_view(request):
#
#     print('test_view')
#
#     json_test = {}
#     json_test['one'] = 'ONE'
#     json_test['two'] = 'TWO'
#
#     return JsonResponse(json_test)
