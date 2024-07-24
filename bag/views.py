from django.shortcuts import render, redirect, reverse, get_object_or_404

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, product_id):
    """ Add quantity of prduct to bag """
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    bag = request.session.get('bag', {})
    if product_id in bag:
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    return redirect(reverse('product_detail', args=[product_id]))