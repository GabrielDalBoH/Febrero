# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class Libros(models.Model):
    cantidad = models.IntegerField(null=True, blank=False)
    autor = models.CharField(max_length=20)



class Prestamo(models.Model):
    libro = models.ForeignKey('Libros', on_delete=models.CASCADE)
    socio = models.ForeignKey('Socio', on_delete=models.CASCADE)
    fecha_de_devolucion = models.DateField(null=True, blank=False)
    libros_prestados = models.IntegerField(null=True, blank=False)




class Socio(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

