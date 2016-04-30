import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Service
import requests


ok_status_codes = [302, 200]


def get_status_code(url, verify=False):
    # try:
    #     r = requests.get(url, verify=verify, timeout=5)
    #     result = r.status_code
    # except:
    #     print('Error making request')
    #     result = 0

    r = requests.get(url, verify=verify, timeout=5)
    result = r.status_code

    return result


def eval_code(status_code):

    local_ok_status_codes = [302, 200]

    if status_code in local_ok_status_codes:
        result = True
    else:
        result = False

    return result



@login_required
def view_status(request):

    print('view_status')
    print(str(request))

    services = Service.objects.order_by('name').values()

    template = loader.get_template('service_status/service_status.html')

    context = RequestContext(request, {'services': services})

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

    return JsonResponse(statuses)


# def ajax(request):
#
#     print('ajax')
#     print(str(request))
#
#     services = Service.objects.order_by('name')
#
#     response = {}
#
#     for service in services:
#         print(service.url)
#         # status_code = get_status_code(service.url)
#         r = requests.get(url, verify=verify, timeout=5)
#         status_code = r.status_code
#         response[service.name] = eval_code(status_code)
#
#     return JsonResponse(response)


def check_service(request):

    print('check_service')
    print(str(request))

    get = request.POST.get

    service_name = get('name')

    service = None

    try:
        service = Service.objects.get(name=service_name)
    except MultipleObjectsReturned:
        print('Multiple objects with name!')
        response = {'error': 'Multiple services with same name'}
    except ObjectDoesNotExist:
        print('Object not found')
        response = {'error': 'No service with given name'}

    if service:
        status_code = get_status_code(service.url)
        response = {service.name: status_code}

    return JsonResponse(response)



# @login_required
# def view_status(request):
#
#     print('view_status')
#     print(str(request))
#
#     services = Service.objects.order_by('name')
#
#     statuses = {}
#
#     for service in services:
#
#         statuses[service.name] = 'Up'
#
#
#     template = loader.get_template('service_status/service_status.html')
#
#     context = RequestContext(request, {'statuses': statuses, })
#
#     return HttpResponse(template.render(context))
