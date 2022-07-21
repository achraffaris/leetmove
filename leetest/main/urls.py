from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('oauth2callback', views.oauth2_callback),
    path('logout', views.logout, name='logout'),
]