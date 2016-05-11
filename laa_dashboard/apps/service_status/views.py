import json
import requests
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView
from django.views.generic.edit import BaseFormView, UpdateView
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.utils import timezone
from .models import Service
from .forms import ServiceForm


class ServiceListView(TemplateView):

    template_name = 'service_status/service_list.html'

    def get_context_data(self, **kwargs):
        context = super(ServiceListView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('name').values()
        return context


class ViewServicesList(ServiceListView):

    link_data = {
        'url_prefix': '../view_status/',
        'type': 'View',
        'view_link': 'javascript:void(0)',
        'update_link': '/services/update_services/',
    }

    def get_context_data(self, **kwargs):
        context = super(ViewServicesList, self).get_context_data(**kwargs)
        context['caption'] = 'View Services'
        context['link_data'] = self.link_data
        return context


class UpdateServicesList(LoginRequiredMixin, ServiceListView):

    link_data = {
        'url_prefix': '../update_status/',
        'type': 'Update',
        'view_link': '/services/view_services/',
        'update_link': 'javascript:void(0)',
    }

    def get_context_data(self, **kwargs):
        context = super(UpdateServicesList, self).get_context_data(**kwargs)
        context['caption'] = 'Update Services'
        context['link_data'] = self.link_data
        return context


class SimpleTable(ServiceListView):

    template_name = 'service_status/simple_table.html'

    # def get_context_data(self, **kwargs):
    #     context = super(SimpleTable, self).get_context_data(**kwargs)
    #     return context


class GetStatuses(View):

    def get(self, request, *args, **kwargs):
        services = Service.objects.order_by('name')
        response = []
        for service in services:
            response.append({'name': service.name,
                             'auto_status': service.auto_status,
                             'manual_status': service.manual_status,
                             'notes': service.notes,
                             })

        return JsonResponse(response, safe=False)


class SingleServiceView(TemplateView):

    template_name = 'service_status/single_service.html'

    def get_service_model(self):
        service_name = self.kwargs['name']
        return Service.objects.get(name=service_name)

    def get_context_data(self, **kwargs):
        context = super(SingleServiceView, self).get_context_data(**kwargs)
        context['service'] = self.get_service_model()
        return context


class ViewServiceStatus(SingleServiceView):

    def get_context_data(self, **kwargs):
        context = super(ViewServiceStatus, self).get_context_data(**kwargs)

        link_data = {
            'view_link': 'javascript:void(0)',
            'update_link': '/services/update_status/%s/' % (self.kwargs['name']),
        }

        context['caption'] = 'View Service'
        context['link_data'] = link_data
        return context


class UpdateServiceStatus(LoginRequiredMixin, UpdateView):

    template_name = 'service_status/single_service.html'
    success_url = '/services/update_services/'
    model = Service
    form_class = ServiceForm
    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super(UpdateServiceStatus, self).get_context_data(**kwargs)

        link_data = {
            'view_link': '/services/view_status/%s/' % (self.kwargs['name']),
            'update_link': 'javascript:void(0)',
        }

        context['caption'] = 'Update Service'
        context['link_data'] = link_data
        return context






