from django.urls import path
from . import views
from .views import add_to_bag


urlpatterns = [
    path(
        '', views.view_bag, name='view_bag'),
    path(
        'add_to_bag/<int:product_id>/',
        add_to_bag, name='add_to_bag'),
    path(
        'remove_from_bag/<int:item_id>/',
        views.remove_from_bag, name='remove_from_bag'),
    path(
        'update_bag/',
        views.update_bag, name='update_bag'),
]
