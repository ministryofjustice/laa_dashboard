import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from .models import Service
import requests
from requests_futures.sessions import FuturesSession
from .forms import ServiceForm, ServiceFormSet

from django.forms import formset_factory, modelform_factory, BaseFormSet

# from django.forms import modelformset_factory



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


# def service_formset_factory(service, form=ServiceForm, formfield_callback=None,
#                          formset=BaseFormSet,
#                          extra=1, can_delete=False, can_order=False,
#                          max_num=None, fields=None, exclude=None):
#     """
#     Returns a FormSet class for the given Django model class.
#     """
#     form = modelform_factory(service, form=form, fields=fields, exclude=exclude,
#                              formfield_callback=formfield_callback)
#     FormSet = formset_factory(form, formset, extra=extra, max_num=max_num,
#                               can_order=can_order, can_delete=can_delete)
#
#     FormSet.model = service
#     return FormSet

# def modelformset_factory(model, form=ModelForm, formfield_callback=None,
#                          formset=BaseModelFormSet,
#                          extra=1, can_delete=False, can_order=False,
#                          max_num=None, fields=None, exclude=None):
#     """
#     Returns a FormSet class for the given Django model class.
#     """
#     form = modelform_factory(model, form=form, fields=fields, exclude=exclude,
#                              formfield_callback=formfield_callback)
#     FormSet = formset_factory(form, formset, extra=extra, max_num=max_num,
#                               can_order=can_order, can_delete=can_delete)
#     FormSet.model = model
#     return FormSet


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
        # create a form instance and populate it with data from the request:
        form = ServiceForm(request.POST, instance=service)
        # check whether it's valid:
        if form.is_valid():

            form.save()

            return HttpResponseRedirect('../update_status/')

    # if a GET (or any other method) we'll create a blank form
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

# def update_status(request):
#
#     # ServiceFormSet = formset_factory(ServiceForm)
#
#     # labels = {
#     #     ''
#     # }
#
#     # ServiceFormSet = modelformset_factory(Service, fields=('manual_status', 'notes'),)
#
#     service_form_set = formset_factory(ServiceForm, formset=ServiceFormSet)
#     print('update_status_new')
#
#     if request.method == 'POST':
#         form_set = service_form_set(request.POST)
#         if form_set.is_valid():
#             form_set.save()
#     else:
#         form_set = service_form_set()
#
#     template = loader.get_template('service_status/update_status.html')
#
#     context = RequestContext(request, {'formset': form_set})
#
#     return HttpResponse(template.render(context))


    # return render(request, 'service_status/update_status.html', {'formset': form_set})

# def update_status(request):
#
#     services = Service.objects.order_by('name')
#
#     sets = []
#
#     for service in services:
#
#         form = ServiceForm(instance=service)
#
#         form_set = { 'name': service.name, 'form': form }
#
#         sets.append(form_set)
#
#     print('update_status')
#
#     template = loader.get_template('service_status/update_status.html')
#
#     context = RequestContext(request, {'sets': sets})
#
#     return HttpResponse(template.render(context))


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


# def check_service(request):
#
#     print('check_service')
#     print(str(request))
#
#     get = request.GET.get
#
#     session = FuturesSession()
#
#     service_name = get('name')
#
#     # print('************' + service_name)
#
#     response = {}
#
#     try:
#         service = Service.objects.get(name=service_name)
#         print(service.url)
#         server_response = session.get(service.url)
#         # status_code = get_status_code(service.url)
#         # response = {'status': status_code}
#     except MultipleObjectsReturned:
#         print('Multiple objects with name!')
#         response = {'error': 'Multiple services with same name'}
#     except ObjectDoesNotExist:
#         print('Object not found')
#         response = {'error': 'No service with given name'}
#
#     # print('*******************' + str(response))
#
#     return JsonResponse(response)

def check_service(request):

    print('check_service')
    print(str(request))

    get = request.GET.get

    service_name = get('name')

    # print('************' + service_name)

    response = {}

    try:
        service = Service.objects.get(name=service_name)
        print(service.url)
        status_code = get_status_code(service.url)
        response = {'status': status_code}
    except MultipleObjectsReturned:
        print('Multiple objects with name!')
        response = {'error': 'Multiple services with same name'}
    except ObjectDoesNotExist:
        print('Object not found')
        response = {'error': 'No service with given name'}

    # print('*******************' + str(response))

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
