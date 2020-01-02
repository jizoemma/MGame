from django.urls import path
from .views import LoginMGame, LogoutMGame

urlpatterns = [
    path('login/', LoginMGame, name='login'),
    path('logout/', LogoutMGame, name='logout'),
]