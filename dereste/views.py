from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView 
from .models import Songs
from .filters import SongsFilter

# Create your views here.

class DeresteIndexView(TemplateView):
  template_name = 'dereste_index.html'

class AllListView(ListView):
  model = Songs
  paginate_by = 20
  template_name = 'dereste_all_list.html'

# Create
class SongCreate(CreateView):
  model = Songs
  fields = ['name','level','type','notes','grade']
  template_name = "dereste_create.html"
  success_url = "../allList"
  #def get_success_url(self):
  #  return reverse('dereste_all_list.html')

# Update
class SongUpdate(UpdateView):
  model = Songs
  fields = ['name','level','type','notes','grade',]

# all List
def song_all_list(request):
    f = SongsFilter(request.GET, queryset=Songs.objects.all())
    return render(request, 'dereste_all_list.html', {'filter': f})

# create detail result