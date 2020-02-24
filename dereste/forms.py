from django import forms
from .models import Songs, Challenges
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# class SelectSingleForm(forms.Form):
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


SONG_TYPE = (
    ('Cute', 'Cute'),
    ('Cool', 'Cool'),
    ('Passion', 'Passion'),
    ('All', 'All'),
  )

DIFFICULTY = (
    ('DEBUT', 'DEBUT'),
    ('REGULAR', 'REGULAR'),
    ('PRO', 'PRO'),
    ('MASTER', 'MASTER'),
    ('MASTER_PLUS', 'MASTER_PLUS'),
    ('Legend_MASTER_PLUS', 'Legend_MASTER_PLUS'),
    ('FORTE', 'FORTE'),
    ('PIANO', 'PIANO'),
    ('LIGHT', 'LIGHT'),
    ('TRICK', 'TRICK')
  )


class SongsRefineForm(forms.Form):
    grade = forms.ChoiceField(label='難易度', choices=DIFFICULTY, required=True, initial='MASTER_PLUS')
    type = forms.ChoiceField(label='タイプ', choices=SONG_TYPE, required=True)
    level = forms.IntegerField(label='レベル', required=False)

    class Meta:
        model = Songs
        fields = [
            'grade', 'type', 'level' 
        ]

#SongsRefineFormSet = forms.formset_factory(SongsRefineForm)


class CreateHelperForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CreateHelperForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_id = 'id-exampleForm'
        #self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        #self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))
