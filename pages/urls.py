from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('faq/', views.faq, name='faq'),
]