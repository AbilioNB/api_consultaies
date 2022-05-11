from django import views
from rest_framework import viewsets, filters
from .serializers import CensoIes_serializer, CensoCurso_serializer
from .models import CensoCurso, CensoIes

class CensoIes_viewset(viewsets.ModelViewSet):
    queryset=CensoIes.objects.all()
    serializer_class=CensoIes_serializer

class CensoCurso_viewset(viewsets.ModelViewSet):
    queryset=CensoCurso.objects.all()
    serializer_class=CensoCurso_serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['co_ies']