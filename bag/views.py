from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from products.models import Product
from django.views.decorators.http import require_POST
from django.contrib import messages


def view_bag(request):
    """
    Renders the shopping bag page,\
    displaying the contents of the user's shopping bag.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered shopping bag page.
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, product_id):
    """
    Adds a specified product to the user's shopping bag,\
    or updates its quantity if it already exists.

    Args:
        request: The HTTP request object.
        product_id: The ID of the product to add to the bag.
    
    Returns:
        HttpResponseRedirect: A redirect to the bag page or the URL specified by the `redirect_url` parameter.
    """
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url') or reverse('view_bag')
    bag = request.session.get('bag', {})
    if str(product_id) in bag:
        bag[str(product_id)] += quantity
        messages.success(
            request,
            f'✓ Updated {product.name} quantity to {bag[str(product_id)]}'
        )
    else:
        bag[str(product_id)] = quantity
        messages.success(
            request,
            f'✓ Added {product.name} to your bag'
        )
    request.session['bag'] = bag
    return redirect(redirect_url)


@require_POST
def remove_from_bag(request, item_id):
    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        if str(item_id) in bag:
            del bag[str(item_id)]
            request.session['bag'] = bag
            messages.success(request, f'Removed {product.name} from your bag')
        return redirect('view_bag')
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return redirect('view_bag')


@require_POST
def update_bag(request):
    try:
        bag = request.session.get('bag', {})
        for item_id, quantity in request.POST.items():
            if item_id.startswith('quantity_'):
                item_id = item_id.split('_')[1]
                try:
                    product = get_object_or_404(Product, pk=item_id)
                    quantity = int(quantity)
                    if quantity > 0:
                        bag[item_id] = quantity
                        messages.success(
                            request,
                            f'Updated {product.name} quantity to {quantity}')
                    else:
                        bag.pop(item_id, None)
                        messages.success(
                            request, f'Removed {product.name} from your bag')
                except (ValueError, Product.DoesNotExist):
                    messages.error(request, 'Invalid update operation')
                    continue
        request.session['bag'] = bag
        return redirect('view_bag')
    except Exception as e:
        messages.error(request, f'Error updating bag: {e}')
        return redirect('view_bag')  # Redirect to the shopping bag page
