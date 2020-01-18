from django import forms
from .models import Songs

class SelectSingleForm(forms.Form):
  songs = forms.ModelChoiceField(models.Songs.objects, label='Song',
          empty_label='Please Select')
