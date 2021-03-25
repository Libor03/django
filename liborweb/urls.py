from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

# Mapování URL adres webu - propojení URL s jejich obsluhou

urlpatterns = [

    # URL "admin/" je namapováno na administrační rozhraní webu

    path('admin/', admin.site.urls),

    # URL "movies/" je namapováno na aplikaci movies a její vlastní soubor 'movies.urls'

    path('movies/', include('movies.urls')),

    # domovská stránka webu ('') je automaticky přesměrována na url z předešlého řádku ('movies')

    path('', RedirectView.as_view(url='movies/')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Metodou static() zajistíme správné mapování adres statických souborů webu (css, js, obrázků atd.).

# Jejich umístění bude definováno konstantami STATIC_URL a STATIC_ROOT v souboru settings.py
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
