from django.contrib import admin
from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.index, name='home'),  # Example home path
    path('cart/', views.cart_view, name='cart'),  # Correctly reference views.cart_view
    path('search/', views.search_results, name='search_results'),
    
]
