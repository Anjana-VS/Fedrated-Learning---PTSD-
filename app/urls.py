from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),  # URL for the welcome page
    path('home/', views.home, name='home'),   # URL for the home page
]
