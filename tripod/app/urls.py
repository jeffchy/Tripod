from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exp/<int:experiment_id>/', views.exp, name='exp'),
    path('config/<int:config_id>/', views.config, name='config'),
]