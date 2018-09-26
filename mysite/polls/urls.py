from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:collegeName>/', views.profile, name='profile'),
    path('objectives/', views.objectives, name='objectives'),
]