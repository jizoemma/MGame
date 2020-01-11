from django.urls import path
from . import views
from .views import LoginMGame, LogoutMGame, Top

appname='loginapp'

urlpatterns = [
    path('', Top.as_view(), name='top'),
    path('login/', LoginMGame.as_view(), name='login'),
    path('logout/', LogoutMGame.as_view(), name='logout'),
    path('user_create/', views.UserCreate.as_view(), name='user_create'),
    path('user_create/done', views.UserCreateDone.as_view(), name='user_create_done'),
    path('user_create/complete/<token>/', views.UserCreateComplete.as_view(), name='user_create_complete'),
]