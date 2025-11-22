from django.db import models
from django.core.exceptions import ValidationError
import re

def validar_nacionalidad_sin_numeros(val: str):
     if re.search(r"\d", val):
        raise ValidationError("La nacionalidad no puede contener números.")

def validar_resumen_minimo(val: str):
    if len(val) < 30:
        raise ValidationError("El resumen debe tener al menos 30 caracteres.")

def validar_calificacion(val: int):
    if val < 1 or val > 5:
        raise ValidationError("La calificación debe estar entre 1 y 5.")
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100, error_messages={'blank': 'El nombre no puede estar vacío.'})
    nacionalidad = models.CharField(
        max_length=100, 
        error_messages={'blank': 'La nacionalidad no puede estar vacía.'}, 
        validators=[validar_nacionalidad_sin_numeros])

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100, error_messages={'blank': 'El titulo no puede estar vacío.'})
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")
    fecha_publicacion = models.DateField()
    resumen = models.TextField(validators=[validar_resumen_minimo])

    def __str__(self):
        return self.titulo
    
class Resena(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name="resenas")
    texto = models.TextField()
    calificacion = models.IntegerField(validators=[validar_calificacion])
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.libro.titulo}: {self.calificacion}/5"
    
