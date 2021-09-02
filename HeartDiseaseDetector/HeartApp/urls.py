# Urls for HeartApp

from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main-page'),
    path('result/', views.pred, name='prediction-page')
]
