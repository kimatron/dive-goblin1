from django.urls import path
from . import views


app_name = 'newsletter'

urlpatterns = [
    path('signup/', views.newsletter_signup, name='newsletter_signup'),
    path('create/', views.create_newsletter, name='create_newsletter'),
    path('unsubscribe/<uuid:token>/', views.unsubscribe, name='newsletter_unsubscribe'),
]
