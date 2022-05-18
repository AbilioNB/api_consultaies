from django import views
from rest_framework import viewsets, filters
from .serializers import CensoIes_serializer, CensoCurso_serializer
from .models import CensoCurso, CensoIes

# Viewsets para cada um dos modelos utilizados.
# Os Cursos são filtrados através do código da IES.
# Único método permitido é GET. 

class CensoIes_viewset(viewsets.ModelViewSet):
    queryset=CensoIes.objects.all()
    serializer_class=CensoIes_serializer
    http_method_names = ['get']

class CensoCurso_viewset(viewsets.ModelViewSet):
    queryset=CensoCurso.objects.all()
    serializer_class=CensoCurso_serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['co_ies']
    http_method_names = ['get']