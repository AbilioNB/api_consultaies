from rest_framework import routers
from .views import CensoIes_viewset, CensoCurso_viewset

# Rotas para cada uma das views. Serão utilizadas nas URLs.

iesrouter=routers.DefaultRouter()
iesrouter.register('ies', CensoIes_viewset)

cursorouter=routers.DefaultRouter()
cursorouter.register('curso', CensoCurso_viewset)