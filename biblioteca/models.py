from django.db import models
from django.core.exceptions import ValidationError

def validar_no_vacio(val: str):
     if not val or not val.strip():
        raise ValidationError("Este campo no puede estar vacío ni tener solo espacios.")
     
def validar_resumen_minimo(val: str):
    if len(val) < 30:
        raise ValidationError("El resumen debe tener al menos 30 caracteres.")

def validar_calificacion(val: int):
    if val < 1 or val > 5:
        raise ValidationError("La calificación debe estar entre 1 y 5.")
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_no_vacio])
    nacionalidad = models.CharField(max_length=100, validators=[validar_no_vacio])

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100, validators=[validar_no_vacio])
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
    
