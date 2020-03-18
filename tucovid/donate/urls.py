from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('donate_history/', views.donate_history, name='donate_history'),
    path('donate/', views.donate, name='donate'),
    path('request_history/', views.request_history, name='request_history'),
    path('request/', views.request, name='request'),
]