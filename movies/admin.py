from django.contrib import admin

# Import všech modelů, které obsahuje models.py

from .models import *
from django.db import models

# Import metod MaxValueValidator, MinValueValidator z balíku django.core.validators

from django.core.validators import MaxValueValidator, MinValueValidator

# Import metody reverse z balíku django.urls - zajistí generování URL obrácením URL patterns

from django.urls import reverse
# Registrace modelů v administraci aplikace

admin.site.register(Genre)
admin.site.register(Film)





