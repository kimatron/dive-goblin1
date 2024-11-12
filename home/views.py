from django.shortcuts import render


def index(request):
    # a view to return the home page
    return render(request, 'home/index.html')


def search_results(request):
    # a view to return the search result page
    return render(request, 'search_results.html')
