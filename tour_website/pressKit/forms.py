from django import forms
from django.forms import ModelForm, Textarea
from .models import *

class shows_form(ModelForm):
    class Meta:
        model = shows
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'type':'text'}),
            'local': forms.CheckboxInput(attrs={}),
            'date': forms.DateInput(attrs={'type':'date'}),
            'time_start': forms.TimeInput(attrs={'type':'time'}),
            'time_end': forms.TimeInput(attrs={'type':'time'}),
            'address': forms.TextInput(attrs={'type':'text'}),
            'city': forms.TextInput(attrs={'type':'text'}),
            'state': forms.TextInput(attrs={'type':'text'}),
            'zipcode': forms.TextInput(attrs={'type':'text'}),
            'description': forms.Textarea(),
            'venue': forms.TextInput(attrs={'type':'text'}),
            'ticket_link': forms.TextInput(attrs={'type':'text'})
        }