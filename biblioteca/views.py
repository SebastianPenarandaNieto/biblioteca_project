from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg
from .models import Libro, Autor, Resena
from .serializers import AutorSerializer, LibroSerializer, ResenaSerializer
from .pagination import AutorPagination, LibroPagination, ResenaPagination

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    pagination_class = AutorPagination

    filterset_fields = ['nombre', 'nacionalidad']
    ordering_fields = ['nombre', 'nacionalidad']

    def perform_create(self, serializer):
        nombre = serializer.validated_data.get('nombre', '').strip()
        nacionalidad = serializer.validated_data.get('nacionalidad', '').strip().title()
        serializer.save(nombre=nombre, nacionalidad=nacionalidad)

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
    pagination_class = LibroPagination

    filterset_fields = ['autor', 'fecha_publicacion']
    ordering_fields = ['titulo', 'fecha_publicacion']

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
    pagination_class = ResenaPagination

    def get_queryset(self):
        if self.request.query_params.get('recent'):
            return Resena.objects.order_by('-fecha')[:20]
        return Resena.objects.all()

