from django.contrib import admin

# Register your models here.

from .models import Service

admin.site.register(Service)

# class ServiceAdmin(admin.ModelAdmin):
#
#     fieldsets = []