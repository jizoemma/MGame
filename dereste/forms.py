from django import forms
from .models import Songs
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class SelectSingleForm(forms.Form):
  songs = forms.ModelChoiceField(models.Songs.objects, label='Song',
          empty_label='Please Select')

class CreateForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super(CreateForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form
    
