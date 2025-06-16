from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    """
    Model representing product categories for organizing dive gear.
    
    Categories help users navigate and filter products by type
    (e.g., scuba gear, wetsuits, accessories).
    """
    class Meta:
        verbose_name_plural = 'categories'
        indexes = [
            models.Index(fields=['name']),
        ]
    
    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        """Return the category name as string representation."""
        return self.name

    def get_friendly_name(self):
        """
        Return the user-friendly display name for the category.
        
        Returns:
            str: The friendly name if available, otherwise the regular name.
        """
        return self.friendly_name


class Product(models.Model):
    """
    Model representing diving equipment and gear products.
    
    Stores all product information including pricing, inventory,
    categorization, and customer ratings for the e-commerce store.
    """
    class Meta:
        indexes = [
            models.Index(fields=['id']),  # Primary key index for faster lookups
            models.Index(fields=['category']),  # For category filtering
            models.Index(fields=['name']),  # For search queries
            models.Index(fields=['-updated_at']),  # For sorting by newest
            models.Index(fields=['price']),  # For price sorting
            models.Index(fields=['rating']),  # For rating sorting
        ]
    
    sku = models.CharField(
        max_length=255, blank=True, null=True,
        help_text="Stock Keeping Unit - unique product identifier")
    name = models.CharField(
        max_length=200,
        help_text="Product name displayed to customers")
    description = models.TextField(
        help_text="Detailed product description and specifications")
    has_sizes = models.BooleanField(
        default=False, null=True, blank=True,
        help_text="Whether this product comes in different sizes")
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        help_text="Product price in USD")
    stock = models.PositiveIntegerField(
        help_text="Current inventory quantity available")
    category = models.ForeignKey(
        'Category', related_name='products',
        blank=True, on_delete=models.CASCADE,
        help_text="Product category for organization")
    image = models.ImageField(
        upload_to='products/', 
        blank=True, 
        null=True,
        default='products/dgdefault.png',
        help_text="Main product image")
    rating = models.DecimalField(
        max_digits=3, decimal_places=1, default=0,
        help_text="Average customer rating (0.0 to 5.0)")
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Timestamp of last product update")

    def __str__(self):
        """Return the product name as string representation."""
        return self.name

    def is_in_stock(self):
        """
        Check if product is currently available for purchase.
        
        Returns:
            bool: True if stock > 0, False otherwise.
        """
        return self.stock > 0

    def get_display_price(self):
        """
        Get formatted price for display.
        
        Returns:
            str: Price formatted as currency string.
        """
        return f"${self.price:.2f}"


class Wishlist(models.Model):
    """
    Model representing a user's wishlist of desired products.
    
    Allows customers to save products they're interested in
    for future purchase consideration.
    """
    class Meta:
        indexes = [
            models.Index(fields=['user']),  # For faster user lookups
        ]
        unique_together = ('user',)  # Ensure one wishlist per user
    
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,
        help_text="User who owns this wishlist")
    products = models.ManyToManyField(
        Product,
        blank=True,
        help_text="Products saved to this wishlist")

    def __str__(self):
        """Return string representation of the wishlist."""
        return f'Wishlist of {self.user.username}'

    def get_product_count(self):
        """
        Get the number of products in this wishlist.
        
        Returns:
            int: Count of products in the wishlist.
        """
        return self.products.count()

    def add_product(self, product):
        """
        Add a product to the wishlist if not already present.
        
        Args:
            product (Product): The product to add to the wishlist.
            
        Returns:
            bool: True if product was added, False if already in wishlist.
        """
        if not self.products.filter(id=product.id).exists():
            self.products.add(product)
            return True
        return False