from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from .models import *
from .serializers import *

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    def perform_create(self, serializer):
        nombre = serializer.validated_data.get('nombre', '').strip()
        nacionalidad = serializer.validated_data.get('nacionalidad', '').strip().title()
        serializer.save(nombre=nombre, nacionalidad=nacionalidad)

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer

    def get_queryset(self):
        if self.request.query_params.get('recent'):
            return Libro.objects.order_by('-fecha_publicacion')[:10]
        return Libro.objects.all()

    @action(detail=True, methods=['get'])
    def promedio_calificaciones(self, request, pk=None):
        libro = self.get_object()
        dic_prom = libro.resenas.aggregate(promedio=Avg('calificacion'))
        prom_val= dic_prom['promedio']
        return Response({'promedio_calificaciones': prom_val})
    

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

    def get_queryset(self):
        if self.request.query_params.get('recent'):
            return Resena.objects.order_by('-fecha')[:20]
        return Resena.objects.all()

