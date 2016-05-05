from django import forms
from .models import Service


class ServiceForm(forms.ModelForm):

    notes = forms.Field(widget=forms.Textarea   , required=False)

    class Meta:
        model = Service
        fields = ('manual_status', 'notes',)


class ServiceFormSet(forms.BaseFormSet):

    pass
