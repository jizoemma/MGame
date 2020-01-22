from django import forms
from .models import Songs
from crispy_forms.helper import FormHelper

class SelectSingleForm(forms.Form):
  songs = forms.ModelChoiceField(models.Songs.objects, label='Song',
          empty_label='Please Select')
  
