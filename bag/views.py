from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from products.models import Product 
from django.views.decorators.http import require_POST

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', reverse('view_bag'))  # Default redirect to a shopping bag view
    
    bag = request.session.get('bag', {})
    if product_id in bag:
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)

def remove_from_bag(request, item_id):
    """ Remove a specified item from the shopping bag """
    
    # Retrieve the current bag from the session
    bag = request.session.get('bag', {})
    
    # Remove the item if it exists
    if item_id in bag:
        del bag[item_id]
    
    # Save the updated bag back to the session
    request.session['bag'] = bag
    
    # Redirect to the bag view
    return redirect('view_bag')

def checkout(request):
    """ Display the checkout page """
    # Add any logic needed for the checkout page here
    return render(request, 'bag/checkout.html')

@require_POST
def update_bag(request):
    # Logic to update quantities in the shopping bag
    # Example:
    bag = request.session.get('bag', {})
    for item_id, quantity in request.POST.items():
        if item_id.startswith('quantity_'):
            item_id = item_id.split('_')[1]
            quantity = int(quantity)
            if quantity > 0:
                bag[item_id] = quantity
            else:
                bag.pop(item_id, None)
    request.session['bag'] = bag
    return redirect('bag')  # Redirect to the shopping bag page