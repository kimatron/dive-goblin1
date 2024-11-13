from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        # Only include URLs that exist in your urls.py
        return ['home']  # Add more as needed

    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return f'/products/{obj.id}'  # Adjust based on your URL pattern
