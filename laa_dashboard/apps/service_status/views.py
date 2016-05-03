import json
import requests
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Service
from .forms import ServiceForm, ServiceFormSet


# ok_status_codes = [302, 200]

# ok_hex_colour = '#009900'
# not_ok_hex_colour = '#e60000'


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


class ServiceListView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('name').values()
        return context


class UpdateStatus(ServiceListView):

    template_name = 'service_status/update_status.html'


class ViewServices(ServiceListView):

    template_name = 'service_status/view_services.html'


class SimpleTable(ServiceListView):

    template_name = 'service_status/simple_table.html'

    def get_context_data(self, **kwargs):
        context = super(SimpleTable, self).get_context_data(**kwargs)
        print(context)
        context['width'] = self.request.GET.get('width', default=300)
        context['height'] = self.request.GET.get('height', default=800)
        # context['use_auto'] = self.request.GET.get('use_auto', default=False)

        return context


def view_status(request):

    service_name = request.GET.get('name')

    try:
        service = Service.objects.get(name=service_name)
    except MultipleObjectsReturned:
        print('Multiple objects with name!')
    except ObjectDoesNotExist:
        print('Object not found')

    print(service_name)

    template = loader.get_template('service_status/view_status.html')
    context = RequestContext(request, {'service': service})

    return HttpResponse(template.render(context))


def edit_status(request):

    service_name = request.GET.get('name')

    try:
        service = Service.objects.get(name=service_name)
    except MultipleObjectsReturned:
        print('Multiple objects with name!')
    except ObjectDoesNotExist:
        print('Object not found')

    print(service_name)

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../update_status/')

    else:
        form = ServiceForm(instance=service)

    template = loader.get_template('service_status/edit_status.html')
    context = RequestContext(request, {'form': form, 'service': service})

    return HttpResponse(template.render(context))


def check_all_services(request):

    print('check_all_services')
    print(str(request))
    services = Service.objects.order_by('name')
    statuses = {}

    for service in services:

        if service.auto_status:
            statuses[service.name] = True
        else:
            statuses[service.name] = False

    return JsonResponse(statuses)





