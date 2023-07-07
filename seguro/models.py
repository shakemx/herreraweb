from django.db import models

from base.models import BaseModel
from empresa.models import Empresa

class Seguro(BaseModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField('Tipo', max_length=200,blank=False, null=False)

    class Meta:
        verbose_name = 'Seguro'
        verbose_name_plural = 'Seguros'

    def __str__(self):
        return self.empresa.nombre + ' - ' + self.nombre 

    
class Producto(BaseModel):
    seguro = models.ForeignKey(Seguro, on_delete=models.CASCADE)
    producto = models.CharField('Producto', max_length=200,blank=False, null=False)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.seguro.nombre + ' - ' + self.producto
    
class TipoSeguro(BaseModel):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tipo = models.CharField('Tipo de Seguro', max_length=200,blank=False, null=False)

    class Meta:
        verbose_name = 'Tipo de Seguro'
        verbose_name_plural = 'Tipos de Seguros'

    def __str__(self):
        return self.producto.seguro.nombre + ' - ' + self.producto.producto + ' - ' + self.tipo
    