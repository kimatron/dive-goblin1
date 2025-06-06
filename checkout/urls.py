from django.urls import path
from . import views
from .webhooks import webhook

app_name = 'checkout'

urlpatterns = [
    path(
        '', views.checkout, name='checkout'),
    path(
        'checkout_success/<order_number>/',
        views.checkout_success, name='checkout_success'),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data, name='cache_checkout_data'),
    path(
        'webhook/',
        webhook, name='webhook'),
    path('order_history/<str:order_number>',
         views.order_history, name='order_history'),
]
