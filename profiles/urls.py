from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<str:order_number>/', views.order_history, name='order_history'),
    path('update/', views.update_account, name='update_account'),
    path('delete/', views.delete_account, name='delete_account'),
]
