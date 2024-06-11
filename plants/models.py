from django.db import models
from django.conf import settings
from django.core.serializers import deserialize
import ast
# Create your models here.
    
class PlanttingType(models.Model):
    label = models.CharField(verbose_name="Label", max_length=50)

    def __str__(self) -> str:
        return self.label

#dar uma olhada no durationField do django
class GrowthStages(models.Model):

    label = models.CharField(verbose_name=("Label"), max_length=50)
    growth_level = models.SmallIntegerField(verbose_name="Nivel de crescimento")

    def __str__(self) -> str:
        return f'{self.label} [{self.growth_level}]'

class Plant (models.Model):
    label = models.CharField(verbose_name="Label", max_length=50)
    min_temperature = models.SmallIntegerField(verbose_name="Temperatura minima")
    max_temperature = models.SmallIntegerField(verbose_name="Temperatura maxima")
    
    min_umidty = models.SmallIntegerField(verbose_name="Umidade minima")
    max_umidty = models.SmallIntegerField(verbose_name="Umidade maxima")
    growth_stages = models.ManyToManyField(GrowthStages, verbose_name="Estados de crescimento")

    def __str__(self) -> str:
        return self.label
    
class Planting (models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=("Dono"), on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(verbose_name="Ativo")
    plant = models.ForeignKey(Plant, verbose_name=("Planta"), on_delete=models.SET_NULL, null=True)
    planting_type = models.ForeignKey(PlanttingType, verbose_name="Tipo de plantio", on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self) -> str:
        return f'Plantio {self.plant.label}#{self.id}'

    def get_avarage_temp(self):
        avgT = 0
        loops = 0
        stacs = self.stac_set.all().first()
        return stacs.collecteddata_set.all().first()
        