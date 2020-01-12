from django.urls import path
from .views import DeresteIndexView

urlpatterns = [
  #path('', views.index, name='index'),
  path('', DeresteIndexView.as_view(), name='dereste'),
]