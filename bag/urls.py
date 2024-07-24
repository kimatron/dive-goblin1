from django.contrib import admin
from django.urls import path
from . import views  # Import your views module
from .views import add_to_bag

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add-to-bag/<int:product_id>/', add_to_bag, name='add_to_bag'),
    
]
