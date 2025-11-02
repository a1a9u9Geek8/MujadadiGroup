"""
URL configuration for mujsettings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from core import views
from core.sitemaps import StaticViewSitemap, CategorySitemap
from core.create_admin_view import create_admin
from core.debug_view import debug_media
from core.sync_view import sync_images

sitemaps = {
    'static': StaticViewSitemap,
    'categories': CategorySitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("careers/", views.careers, name="careers"),
    path("contact/", views.contact, name="contact"),
    path("business/<slug:slug>/", views.category_detail, name="category_detail"),
    path("agriculture/", views.agriculture_detail, name="agriculture_detail"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("terms-of-service/", views.terms_of_service, name="terms_of_service"),
    path("investor-relations/", views.investor_relations, name="investor_relations"),
    path("sustainability/", views.sustainability, name="sustainability"),
    path("news-media/", views.news_media, name="news_media"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('create-admin/', create_admin, name='create_admin'),
    path('debug-media/', debug_media, name='debug_media'),
    path('sync-images/', sync_images, name='sync_images'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

