from django.urls import path
from .views import DeresteIndexView, AllListView

urlpatterns = [
  #path('', views.index, name='index'),
  path('', DeresteIndexView.as_view(), name='dereste'),
  path('allList/', AllListView.as_view(), name='allList'),
]