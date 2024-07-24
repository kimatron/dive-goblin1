from django.contrib import admin
from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.view_bag, name='view_bag')
]
