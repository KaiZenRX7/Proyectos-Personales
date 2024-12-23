from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Gestion de Inventario Pañoles",
        default_version='v1',
        description="Documentacion Interactiva de la API de Gestion de Inventario de Pañoles",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="soportepañoles@pañoles.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
