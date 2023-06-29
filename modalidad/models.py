from django.db import models

from base.models import BaseModel
from seguro.models import TipoSeguro


class Modalidad(BaseModel):
    seguro =models.ForeignKey(TipoSeguro, on_delete=models.CASCADE)
    imagen_activos = models.ImageField('Portada', blank=True, default=None, null=True)
    imagen_activos2 = models.ImageField('Contenido', blank=True, default=None, null=True)
    url_video = models.URLField(blank=True, default=None, null=True)
    nombre = models.CharField(max_length=100, blank=True, default=None, null=True)
    definicion = models.TextField(null=True, default=None, blank=True)
    beneficio = models.TextField(null=True, default=None, blank=True)
    elegibilidad = models.TextField(null=True, default=None, blank=True)
    exepciones = models.TextField(null=True, default=None, blank=True)
    adicionales = models.TextField(null=True, default=None, blank=True)
    caracteristicas = models.TextField(null=True, default=None, blank=True)

    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidades'

    def __str__(self):
        return self.nombre
    