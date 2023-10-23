
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home_page, name='home_page'),
    path('search/', views.search, name='search'),
    path('about/', views.about, name='about'),
]
