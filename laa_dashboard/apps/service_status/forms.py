from django import forms
# from django.forms import BaseFormSet

from .models import Service


class ServiceForm(forms.ModelForm):

    notes = forms.Field(widget=forms.Textarea, required=False)

    class Meta:
        model = Service
        fields = ('manual_status', 'notes',)


# ServiceFormSet = formset_factory(ServiceForm)

class ServiceFormSet(forms.BaseFormSet):

    pass
