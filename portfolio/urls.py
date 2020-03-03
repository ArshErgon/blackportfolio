from django.urls import path
from .sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap
from . import views

sitemaps = {
    'home': StaticViewSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
]