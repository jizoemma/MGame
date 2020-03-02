from django import forms
from .models import Songs, Challenges
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.utils import timezone

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


COMBO_EVAL =(
    ("x","x"),
    ("C","C"),
    ("B","B"),
    ("A","A"),
    ("S","S"),
)


class ChallengesDetailCreateForm(forms.Form):
    cdate = forms.DateField(initial=timezone.now(), disabled=True)
    # song_id = forms.CharField(disabled=True)
    score = forms.IntegerField(initial=0)
    perfect = forms.IntegerField(initial=0)
    great = forms.IntegerField(initial=0)
    nice = forms.IntegerField(initial=0)
    bad = forms.IntegerField(initial=0)
    miss = forms.IntegerField(initial=0)
    result = forms.ChoiceField(label='コンボ評価', choices=COMBO_EVAL, required=True, initial='x')
    combo = forms.IntegerField(initial=0)


class CreateHelperForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CreateHelperForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_id = 'id-exampleForm'
        #self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        #self.helper.form_action = 'submit_survey'
        self.helper.add_input(Submit('submit', 'Submit'))
