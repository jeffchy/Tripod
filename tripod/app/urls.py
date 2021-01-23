from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exp/<int:experiment_id>/', views.exp, name='exp'),
    path('config/<int:config_id>/', views.config, name='config'),
    path('exp/add/', views.addexp, name='addexp'),
    path('config/add/<int:experiment_id>', views.addconfig, name='addconfig'),
]