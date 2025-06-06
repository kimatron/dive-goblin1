from django.contrib import admin
from .models import Category, Product, Wishlist


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku', 'name', 'description',
        'category', 'price', 'stock', 'image',
        )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'friendly_name', 'description', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Wishlist)
