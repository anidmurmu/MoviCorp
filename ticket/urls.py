from django.contrib import admin
from django.urls import path, include
from ticket import views

urlpatterns = [
    path('', views.all_tickets),
]
