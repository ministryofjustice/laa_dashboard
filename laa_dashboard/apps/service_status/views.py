import json
import requests
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Service
from .forms import ServiceForm, ServiceFormSet


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


def update_status(request):

    services = Service.objects.order_by('name').values()

    template = loader.get_template('service_status/update_status.html')

    context = RequestContext(request, {'services': services})

    return HttpResponse(template.render(context))


def edit_status(request):

    service_name = request.GET.get('name')
    service = Service.objects.get(name=service_name)
    print(service_name)

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../update_status/')

    else:
        try:
            service = Service.objects.get(name=service_name)
            form = ServiceForm(instance=service)
        except MultipleObjectsReturned:
            print('Multiple objects with name!')
        except ObjectDoesNotExist:
            print('Object not found')

    template = loader.get_template('service_status/edit_status.html')
    context = RequestContext(request, {'form': form})

    return HttpResponse(template.render(context))


def check_all_services(request):

    print('check_all_services')
    print(str(request))
    services = Service.objects.order_by('name')
    statuses = {}

    for service in services:

        try:
            print('Getting ' + service.url)
            r = requests.get(service.url, verify=False, timeout=5)
        except Exception as e:
            print('**********Requests Error *******************:  ', e)

        if r.status_code and r.status_code in ok_status_codes:
            statuses[service.name] = True
        else:
            statuses[service.name] = False

    return JsonResponse(statuses)





