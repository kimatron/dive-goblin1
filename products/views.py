"""
Product views for Dive Goblin e-commerce platform.

Handles product display, search, filtering, CRUD operations,
and wishlist functionality for the diving equipment store.
"""

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product, Category, Wishlist
from .forms import ProductForm


def all_products(request):
    """
    Display all products with filtering, search, and pagination.

    Handles category filtering, search queries, sorting options,
    and pagination for the product catalog.
    
    Args:
        request (HttpRequest): The HTTP request object with GET parameters.
        
    Returns:
        HttpResponse: Rendered products page with filtered/sorted product list.
    """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products:products'))

            queries = Q(
                name__icontains=query) | Q(
                    description__icontains=query)
            products = products.filter(queries)

    # Pagination
    paginator = Paginator(products, 12)  # Show 12 products per page
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page
        products = paginator.page(paginator.num_pages)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    Display detailed information for a single product.
    
    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to display.
        
    Returns:
        HttpResponse: Rendered product detail page.
        
    Raises:
        Http404: If product with given ID doesn't exist.
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def product_management(request):
    """
    Display product management interface for superusers.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Rendered product management page or redirect if unauthorized.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/product_management.html', context)


@login_required
def add_product(request):
    """
    Add a new product to the store (superuser only).
    
    Args:
        request (HttpRequest): The HTTP request object with form data.
        
    Returns:
        HttpResponse: Rendered add product page or redirect after successful creation.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('products:product_management'))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit an existing product (superuser only).
    
    Args:
        request (HttpRequest): The HTTP request object with form data.
        product_id (int): The ID of the product to edit.
        
    Returns:
        HttpResponse: Rendered edit product page or redirect after successful update.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('products:product_management'))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store (superuser only).
    
    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to delete.
        
    Returns:
        HttpResponseRedirect: Redirect to product management page with success message.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product_name = product.name  # Store name before deletion
    product.delete()
    messages.success(request, f'Product "{product_name}" has been deleted!')
    return redirect(reverse('products:product_management'))


@login_required
def add_to_wishlist(request, product_id):
    """
    Add a product to the user's wishlist.
    
    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to add to wishlist.
        
    Returns:
        HttpResponseRedirect: Redirect to wishlist page with success message.
    """
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    messages.success(
        request, f'{product.name} has been added to your wishlist!')
    return redirect('products:wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    """
    Remove a product from the user's wishlist.
    
    Args:
        request (HttpRequest): The HTTP request object.
        product_id (int): The ID of the product to remove from wishlist.
        
    Returns:
        HttpResponseRedirect: Redirect to wishlist page with success message.
    """
    product = get_object_or_404(Product, id=product_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    wishlist.products.remove(product)
    messages.success(
        request, f'{product.name} has been removed from your wishlist!')
    return redirect('products:wishlist')


@login_required
def wishlist(request):
    """
    Display the user's wishlist.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: Rendered wishlist page with user's saved products.
    """
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(
        request, 'products/wishlist.html', {'wishlist': wishlist})