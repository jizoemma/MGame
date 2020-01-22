import django_filters
from .models import Songs

class SongsFilter(django_filters.FilterSet):
  SONG_TYPE = (
    ('Cute','Cu'),
    ('Cool', 'Co'),
    ('Passion','Pa'),
    ('All', 'All'),
  )
  DIFFICULTY = (
    ('DEBUT','DEBUT'),
    ('REGULAR','REGULAR'),
    ('PRO','PRO'),
    ('MASTER','MASTER'),
    ('MASTER_PLUS','MASTER_PLUS'),
    ('Legend_MASTER_PLUS','Legend_MASTER_PLUS'),
    ('FORTE','FORTE'),
    ('PIANO','PIANO'),
    ('LIGHT','LIGHT'),
    ('TRICK','TRICK'),
  )
  grade = django_filters.ChoiceFilter(choices=DIFFICULTY)
  type = django_filters.ChoiceFilter(choices=SONG_TYPE)
  name = django_filters.CharFilter(lookup_expr='contains')
  
  class Meta:
    model = Songs
    fields = [
      'level',
    ]