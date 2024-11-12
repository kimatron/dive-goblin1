from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    sku = models.CharField(
        max_length=255, blank=True, null=True)
    name = models.CharField(
        max_length=200)
    description = models.TextField()
    has_sizes = models.BooleanField(
        default=False, null=True, blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(
        'Category', related_name='products',
        blank=True, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='products/', blank=True, null=True)
    rating = models.DecimalField(
        max_digits=3, decimal_places=1, default=0)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Wishlist of {self.user.username}'
