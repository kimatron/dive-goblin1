from django.urls import path
from . import views

app_name = 'newsletter'

urlpatterns = [
    path('signup/', views.newsletter_signup, name='signup'),
    path('create/', views.create_newsletter, name='create'),
    path('unsubscribe/<str:token>/', views.unsubscribe, name='unsubscribe'),
]