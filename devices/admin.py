from django.contrib import admin
from .models import CollectedData, StacVersion, Stac
# Register your models here.
admin.site.register((CollectedData, StacVersion, Stac))