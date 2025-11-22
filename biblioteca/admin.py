from django.contrib import admin
from .models import Autor, Libro, Resena

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad')
    search_fields = ('nombre',)
    list_filter = ('nombre', 'nacionalidad')
    ordering = ('nombre',)
    list_per_page = 20

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    search_fields = ('titulo','autor__nombre')
    list_filter = ('autor', 'fecha_publicacion')
    ordering = ('autor', '-fecha_publicacion')
    list_per_page = 20
    date_hierarchy = "fecha_publicacion"


@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('libro', 'calificacion')
    search_fields = ('libro__titulo',)
    list_filter = ('calificacion',)
    ordering = ('-calificacion',)
    list_per_page = 20

