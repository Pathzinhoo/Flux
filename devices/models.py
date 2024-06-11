from django.db import models
from plants.models import Planting

class StacVersion(models.Model):
    
    label = models.CharField(max_length=50)
    get_temperature = models.BooleanField(verbose_name="Coleta temperatura")
    get_pressure = models.BooleanField(verbose_name="Coleta pressão")
    get_vibration = models.BooleanField(verbose_name="Coleta vibração")
    get_umidity = models.BooleanField(verbose_name="Coleta umidade")

    def __str__(self) -> str:
        return self.label

class Stac(models.Model):

    version = models.ForeignKey(StacVersion, on_delete=models.SET_NULL, null=True)
    planting =  models.ForeignKey(Planting, verbose_name="Plantio", on_delete=models.SET_NULL, null=True)
    active = models.BooleanField(verbose_name="Ativo")

    def __str__(self) -> str:
        return f'{self.version} -- {self.planting}'

class CollectedData(models.Model):

    stac = models.ForeignKey(Stac, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(verbose_name="Criado", auto_now_add=True)
    data = models.JSONField(verbose_name="Dados")

    def __str__(self) -> str:
        return f'Data#{self.id}'