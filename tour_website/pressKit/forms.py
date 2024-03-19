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
        
class socialLinks_form(ModelForm):
    class Meta:
        model = socialLinks
        fields = ('__all__')
        widgets = {
            'artistName': forms.TextInput(attrs={'type':'text'}),
            'instagram': forms.TextInput(attrs={'type':'text'}),
            'youtube': forms.TextInput(attrs={'type':'text'}),
            'spotify': forms.TextInput(attrs={'type':'text'}),
            'spotifyURI': forms.TextInput(attrs={'type':'text'}),
            'apple': forms.TextInput(attrs={'type':'text'}),
            'twitterX': forms.TextInput(attrs={'type':'text'}),
            'facebook': forms.TextInput(attrs={'type':'text'}),
            'tiktok': forms.TextInput(attrs={'type':'text'}),
            'snapchat': forms.TextInput(attrs={'type':'text'}),
            'soundcloud': forms.TextInput(attrs={'type':'text'}),
        }