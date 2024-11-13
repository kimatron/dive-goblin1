from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, ProductSitemap


# Robots.txt view
def robots_txt(request):
    content = """User-agent: *
Allow: /
Disallow: /accounts/
Disallow: /checkout/
Disallow: /bag/
Disallow: /admin/
Disallow: /profile/

Sitemap: https://dive-goblin-30c473dd6e64.herokuapp.com/sitemap.xml"""
    return HttpResponse(content, content_type="text/plain")


sitemaps = {
    'static': StaticViewSitemap,
    'products': ProductSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls', namespace='profiles')),
    path('newsletter/', include('newsletter.urls')),
    path('pages/', include('pages.urls')),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
