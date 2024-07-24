from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from products.models import Product 

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
    """ Remove an item from the shopping bag """
    bag = request.session.get('bag', {})
    
    # Remove the item if it exists in the bag
    if item_id in bag:
        del bag[item_id]
        request.session['bag'] = bag

    return redirect('view_bag')  # Redirect to the view_bag page or any other page

def checkout(request):
    """ Display the checkout page """
    # Add any logic needed for the checkout page here
    return render(request, 'bag/checkout.html')