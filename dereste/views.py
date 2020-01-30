from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import  UpdateView, DeleteView 
from .models import Songs
from .filters import SongsFilter
from .forms import CreateSongForm, CreateHelperForm
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView,ListView,DetailView, CreateView

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
  form_class = CreateSongForm
  #form_class = CreateHelperForm
  template_name = "dereste_create.html"
  success_url = "../allList"

# Update
class SongUpdate(UpdateView):
  model = Songs
  fields = ['name','level','type','notes','grade',]

# all List
def song_all_list(request):
    f = SongsFilter(request.GET, queryset=Songs.objects.all())
    return render(request, 'dereste_all_list.html', {'filter': f})

# Delete
class SongDelete(DeleteView):
  template_name = 'songs_confirm_delete.html'
  model = Songs
  success_url = reverse_lazy('allList')