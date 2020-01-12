from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

class DeresteIndexView(TemplateView):
  template_name = 'dereste_index.html'

