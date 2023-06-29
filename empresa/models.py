from django.db import models

from base.models import BaseModel

class Empresa(BaseModel):
    nombre = models.CharField('Compañía/Agente de Seguro', max_length=200,blank=False, null=False)
    logo = models.ImageField('Logo Empresa',blank=False,null=False)
    direccion = models.CharField('Dirección',max_length=200)
    telefono = models.CharField('Teléfono',max_length=12, blank=True, null=True)
    movil = models.CharField('Celular',max_length=12)
    email = models.EmailField('Correo',max_length=254)
    facebook = models.URLField('Facebook', blank=True, null=True)
    instagram = models.URLField('Instagram', blank=True, null=True)
    twitter = models.URLField('Twitter', blank=True, null=True)
    linkedin = models.URLField('Linkedin', blank=True, null=True)
    youtube = models.URLField('Youtube', blank=True, null=True)
    whatsapp = models.URLField('Whatsapp', blank=True, null=True)


    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nombre

    
