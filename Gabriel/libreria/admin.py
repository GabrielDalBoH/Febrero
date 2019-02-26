# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from.models import Libros, Prestamo, Socio


class Librosadmin(admin.ModelAdmin):
    list_display=('cantidad', 'autor',)

class Prestamoadmin(admin.ModelAdmin):
    list_display=('libro', 'libros_devueltos', 'libros_nodevueltos',)


class Socioadmin(admin.ModelAdmin):
    list_display=('nombre', 'apellido', )








admin.site.register(Libros)
admin.site.register(Prestamo)
admin.site.register(Socio)