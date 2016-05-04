import json
import requests
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView
from django.views.generic.edit import BaseFormView
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

    def get_context_data(self, **kwargs):
        context = super(ViewServicesList, self).get_context_data(**kwargs)
        context['service_click_link'] = '../view_status/'
        return context


class UpdateServicesList(ServiceListView):

    def get_context_data(self, **kwargs):
        context = super(UpdateServicesList, self).get_context_data(**kwargs)
        context['service_click_link'] = '../update_status/'
        return context


class SimpleTable(ServiceListView):

    template_name = 'service_status/simple_table.html'

    def get_context_data(self, **kwargs):
        context = super(SimpleTable, self).get_context_data(**kwargs)
        print(context)
        context['width'] = self.request.GET.get('width', default=300)
        context['height'] = self.request.GET.get('height', default=800)
        # context['use_auto'] = self.request.GET.get('use_auto', default=False)
        context['last_refresh'] = timezone.now()

        return context


class GetStatuses(View):

    def get(self, request, *args, **kwargs):
        services = Service.objects.order_by('name')
        response = []
        for service in services:
            response.append({'name': service.name,
                             'auto_status': service.auto_status,
                             'manual_status': service.manual_status
                             })

        return JsonResponse(response, safe=False)


class SingleServiceView(TemplateView):

    template_name = 'service_status/single_service.html'

    def get_service_model(self):
        service_name = self.request.GET.get('name')
        service = Service.objects.get(name=service_name)
        return service

    def get_context_data(self, **kwargs):
        context = super(SingleServiceView, self).get_context_data(**kwargs)
        context['service'] = self.get_service_model()

        return context


class ViewServiceStatus(SingleServiceView):

    pass


class UpdateServiceStatus(SingleServiceView, BaseFormView):

    def post(self, request, *args, **kwargs):
        service = self.get_service_model()
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../update_status/')

    def get(self, request, *args, **kwargs):
        service = self.get_service_model()
        form = ServiceForm(instance=service)
        template = loader.get_template(self.template_name)
        context = RequestContext(self.request, {'form': form, 'service': service})
        return HttpResponse(template.render(context))







