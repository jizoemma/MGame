from django.urls import path
from .views import DeresteIndexView, AllListView, SongCreate, SongUpdate, SongDelete, ChallengesCreate
from dereste import views

urlpatterns = [
  # path('', views.index, name='index'),
  path('', DeresteIndexView.as_view(), name='dereste'),
  # path('allList/', AllListView.as_view(), name='allList'),
  path('allList/', views.song_all_list, name='allList'),
  path('create/', views.SongCreate.as_view(), name='create'),
  path('delete/<int:pk>/', views.SongDelete.as_view(), name='delete'),
  path('update/<int:pk>/', views.SongUpdate.as_view(), name='update'),
  path('ch_create/', views.ChallengesCreate.as_view(), name='ch_create'),
  path('ch_allList/', views.challenges_all_list, name='ch_allList'),
  path('ch_delete/<int:pk>/', views.ChallengesDelete.as_view(), name='ch_delete'),
]