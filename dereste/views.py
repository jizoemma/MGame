from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Songs

# Create your views here.

class DeresteIndexView(TemplateView):
  template_name = 'dereste_index.html'

class AllListView(ListView):
  model = Songs
  paginate_by = 20
  template_name = 'dereste_all_list.html'
