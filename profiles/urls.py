from django.urls import path
from . import views


app_name = 'profiles'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('update-account/', views.update_account, name='update_account'),
    path('delete-account/', views.delete_account, name='delete_account'),
]
