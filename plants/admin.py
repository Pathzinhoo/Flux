from django.contrib import admin
from .models import GrowthStages, Plant, Planting, PlanttingType
# Register your models here.

admin.site.register((GrowthStages, Plant, PlanttingType, Planting))