from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Songs
from .filters import SongsFilter

# Create your views here.

class DeresteIndexView(TemplateView):
  template_name = 'dereste_index.html'

class AllListView(ListView):
  model = Songs
  paginate_by = 20
  template_name = 'dereste_all_list.html'

def song_all_list(request):
    f = SongsFilter(request.GET, queryset=Songs.objects.all())
    return render(request, 'dereste_all_list.html', {'filter': f})