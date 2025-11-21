from django.contrib import admin
from models import *

class AutorAdmin(admin.ModelAdmin):
    pass

class LibroAdmin(admin.ModelAdmin):
    pass

class ResenaAdmin(admin.ModelAdmin):
    pass


admin.register(Autor, AutorAdmin)
admin.register(Libro, LibroAdmin)
admin.register(Resena, ResenaAdmin)
