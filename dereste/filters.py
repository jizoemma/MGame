import django_filters
from .models import Songs

class SongsFilter(django_filters.FilterSet):
  class Meta:
    model = Songs
    fields = '__all__'