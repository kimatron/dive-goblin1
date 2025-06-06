from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_control

@cache_control(max_age=60 * 60 * 24)  # Cache for 24 hours
def favicon(request):
    # SVG emoji favicon
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
        <text y=".9em" font-size="90">🤿</text>
    </svg>'''
    
    return HttpResponse(svg_content, content_type='image/svg+xml')

def index(request):
    # a view to return the home page
    return render(request, 'home/index.html')


def search_results(request):
    # a view to return the search result page
    return render(request, 'search_results.html')
