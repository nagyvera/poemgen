from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('generator/', views.generator, name='generator'),
    path('yourpoem/', views.yourpoem, name='yourpoem'),
]
