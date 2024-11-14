from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about_view, name='about'),
    path('faq/', views.faq_view, name='faq'),
    path('privacy/', views.privacy_view, name='privacy'),
    path('terms/', views.terms, name='terms'),
]
