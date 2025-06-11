from decimal import Decimal, ROUND_HALF_UP
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from products.models import Product


def bag_contents(request):
    """
    Optimized bag contents context processor with caching
    """
    # Create cache key based on session and bag contents
    bag = request.session.get('bag', {})
    bag_hash = hash(str(sorted(bag.items())))
    cache_key = f"bag_contents_{request.session.session_key}_{bag_hash}"
    
    # Try to get cached result
    cached_contents = cache.get(cache_key)
    if cached_contents:
        return cached_contents
    
    # Calculate bag contents
    bag_items = []
    total = Decimal('0.00')
    product_count = 0

    for item_id, quantity in bag.items():
        try:
            product = get_object_or_404(Product, pk=item_id)
            item_total = Decimal(quantity) * product.price
            total += item_total
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'total_price': item_total
            })
        except:
            # Handle case where product doesn't exist
            continue

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')
    
    grand_total = delivery + total
    
    # Round values to 2 decimal places
    total = total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    delivery = delivery.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    grand_total = grand_total.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    # Cache for 5 minutes (300 seconds)
    cache.set(cache_key, context, 300)
    return context