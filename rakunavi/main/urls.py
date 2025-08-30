from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('program/', views.program_list, name='program_list'),
    path('program/<int:number>/', views.program_detail, name='program_detail'),
    path('team/', views.team, name='team'),
]
