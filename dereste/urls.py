from django.urls import path
from .views import DeresteIndexView, AllListView
from dereste import views

urlpatterns = [
  #path('', views.index, name='index'),
  path('', DeresteIndexView.as_view(), name='dereste'),
  #path('allList/', AllListView.as_view(), name='allList'),
  path('allList/', views.song_all_list, name='allList'),
  path('create/', views.SongCreate.as_view(), name='create'),
  path('delete/<int:pk>/', views.SongDelete.as_view(), name='delete'),
]