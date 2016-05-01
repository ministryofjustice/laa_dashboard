from django import forms
# from django.forms import formset_factory

from .models import Service


class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('manual_status', 'notes',)


# ServiceFormSet = formset_factory(ServiceForm)
