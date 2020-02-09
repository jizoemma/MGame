from django import forms
from .models import Songs, Challenges
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

#class SelectSingleForm(forms.Form):
#  songs = forms.ModelChoiceField(models.Songs.objects, label='Song',
#          empty_label='Please Select')

class CreateSongForm(forms.ModelForm):
  class Meta:
    model = Songs
    fields = ("name", "level","type","notes","grade",)

class CreateChallengesForm(forms.ModelForm):
  class Meta:
    model = Challenges
    fields = ("song_id","score","perfect","great",
              "nice", "bad", "miss", "result", "combo")


class CreateHelperForm(forms.Form):
  def __init__(self, *args, **kwargs):
    super(CreateHelperForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    #self.helper.form_id = 'id-exampleForm'
    #self.helper.form_class = 'blueForms'
    self.helper.form_method = 'post'
    #self.helper.form_action = 'submit_survey'
    self.helper.add_input(Submit('submit', 'Submit'))
