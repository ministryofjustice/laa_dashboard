from django.contrib import admin
from kombu.transport.django import models as kombu_models
from .models import Service

admin.site.register(Service)

admin.site.register(kombu_models.Message)
