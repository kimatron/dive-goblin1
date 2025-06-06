from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path(
        '', views.all_products, name='products'),
    path(
        '<int:product_id>/',
        views.product_detail, name='product_detail'),
    path(
        'manage/',
        views.product_management, name='product_management'),
    path(
        'add/',
        views.add_product, name='add_product'),
    path(
        'edit/<int:product_id>/',
        views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>/',
        views.delete_product, name='delete_product'),
    path(
        'wishlist/',
        views.wishlist, name='wishlist'),
    path(
        'wishlist/add/<int:product_id>/',
        views.add_to_wishlist, name='add_to_wishlist'),
    path(
        'wishlist/remove/<int:product_id>/',
        views.remove_from_wishlist, name='remove_from_wishlist'),
]
