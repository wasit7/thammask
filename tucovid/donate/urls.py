from django.urls import path
from . import views
app_name = 'donate'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('donate/', views.donate, name='donate'),
    path('request/', views.request, name='request'),
    path('review/', views.review, name='review'),
    path('verify_user', views.verify_user, name='check_user_exists'),
    path('printing/', views.printing, name='printing')
]