from django.shortcuts import render

# Create your views here.
def index(request):
    # a view to return the home page
    return render(request, 'home/index.html')

def cart_view(request):
    # Your cart view logic here
    return render(request, 'cart.html')