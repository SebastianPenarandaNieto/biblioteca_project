from rest_framework import serializers
from .models import Autor, Libro, Resena

class AutorSerializer(serializers.ModelSerializer):
    libros_recientes = serializers.SerializerMethodField()

    def get_libros_recientes(self, obj):
        libros = obj.libros.order_by('-fecha_publicacion')[:5]
        return LibroSerializer(libros, many=True).data

    class Meta:
        model = Autor
        fields = ['id', 'nombre', 'nacionalidad', 'libros_recientes']

    
class LibroSerializer(serializers.ModelSerializer):

    resenas_recientes = serializers.SerializerMethodField()
    nombre_autor = serializers.ReadOnlyField(source='autor.nombre')

    def get_resenas_recientes(self, obj):
        resenas = obj.resenas.order_by('-fecha')[:5]
        return ResenaSerializer(resenas, many=True).data

    class Meta:
        model = Libro
        fields = ['id', 'titulo', 'autor', 'nombre_autor', 'fecha_publicacion', 'resenas_recientes']



class ResenaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Resena
        fields = ['id', 'libro', 'texto', 'calificacion', 'fecha']

    