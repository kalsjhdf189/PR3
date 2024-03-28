from django.contrib import admin
from django.urls import path
from PR3 import views

urlpatterns = [
    path('', views.index),
    path('first/', views.first),
]
