from django.db import models

from base.models import BaseModel
from empresa.models import Empresa

class Agente(BaseModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField('Agente',max_length=200)
    imagen = models.ImageField('Foto Agente',blank=False,null=False)
    portada = models.ImageField('Portada Presentación',blank=False,null=False)
    bio = models.TextField('Biografía',default='Profesional de Seguros, experto en prevención de riesgos y cuidado patrimonial', null=False, blank=False)
    perfil = models.CharField('Puesto', default='Agente de Seguros', null=False, blank=False)
    url_ubicacion = models.URLField('URL Google Maps', blank=False, null=False)
    direccion = models.CharField('Lugar de Trabajo',max_length=200)
    horario = models.CharField('Horario Laboral', default='Lun - Vie 9 a 18 hrs', null=False, blank=False)
    telefono = models.CharField('Teléfono',max_length=12, blank=True, null=True)
    movil = models.CharField('Celular',max_length=12)
    email = models.EmailField('Correo',max_length=254, blank=True, null=True)
    facebook = models.URLField('Facebook', blank=True, null=True)
    instagram = models.URLField('Instagram', blank=True, null=True)
    twitter = models.URLField('Twitter', blank=True, null=True)
    linkedin = models.URLField('Linkedin', blank=True, null=True)
    youtube = models.URLField('Youtube', blank=True, null=True)
    whatsapp = models.URLField('Whatsapp', blank=True, null=True)

    class Meta:
        verbose_name = 'Agente'
        verbose_name_plural = 'Agentes'

    def __str__(self):
        return self.nombre
