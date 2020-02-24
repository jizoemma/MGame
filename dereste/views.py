from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import DeleteView, UpdateView
from .models import Songs, Challenges
from .filters import SongsFilter, ChallengesFilter
from .forms import CreateSongForm, CreateChallengesForm, SongsRefineForm
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from django.template import RequestContext
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
    # form_class = CreateHelperForm
    template_name = "dereste_create.html"
    success_url = "../allList"

# Update


class SongUpdate(UpdateView):
    model = Songs
    fields = ['name', 'level', 'type', 'notes', 'grade']
    template_name = "songs_update_form.html"
    success_url = reverse_lazy('allList')

# songs all List


def song_all_list(request):
    f = SongsFilter(request.GET, queryset=Songs.objects.all())
    return render(request, 'dereste_all_list.html', {'filter': f})

# Songs Delete


class SongDelete(DeleteView):
    template_name = 'songs_confirm_delete.html'
    model = Songs
    success_url = reverse_lazy('allList')

# Challenges Delete


class ChallengesDelete(DeleteView):
    template_name = 'challenges_confirm_delete.html'
    model = Challenges
    success_url = reverse_lazy('ch_allList')


class ChallengesCreate(CreateView):
    model = Challenges
    form_class = CreateChallengesForm
    template_name = "dereste_challenges_create.html"
    success_url = "../ch_allList"

# challenges all List


def challenges_all_list(request):
    f = ChallengesFilter(request.GET, queryset=Challenges.objects.all())
    return render(request, 'dereste_challenges_all_list.html', {'filter': f})

# ChallengesUpdate


class ChallengesUpdate(UpdateView):
    model = Challenges
    fields = ['score', 'perfect', 'great', 'nice', 'bad', 'miss', 'result', 'combo', ]
    template_name = "challenges_update_form.html"
    success_url = reverse_lazy('ch_allList')


def refine(request):
    
    form = SongsRefineForm()
    song_list = Songs.objects.all()
    
    if request.method == 'POST':
        grade_data = request.POST.get('grade')
        type_data = request.POST.get('type')
        level_data = request.POST.get('level')
        if level_data == '':
            song_list = song_list.filter(grade=grade_data).filter(type=type_data)
        else:
            song_list = song_list.filter(grade=grade_data).filter(type=type_data).filter(level=level_data)
    
    context = {'form': form, 'song_list': song_list}
    return render(request, 'dereste_challenges_select.html', context)
