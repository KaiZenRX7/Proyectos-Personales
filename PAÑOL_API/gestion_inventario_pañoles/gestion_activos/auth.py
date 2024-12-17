from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

#Documentacion del endpoint para obtener el token

token_obtain_schema = swagger_auto_schema(
    operation_description = "Obtener un token JWT con las credenciales del usuario",
    reques_body= openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de usuario'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña del usuario'),
        },
        required=['username', 'password']
    ),
    responses={
        200:openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'access': openapi.Schema(type=openapi.TYPE_STRING, description='Token de acceso JWT'),
                'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Token de refresco JWT'),
            },
        ),
        401: 'Credenciales invalidas',
    }
)


# Documentación para el endpoint de refresco de tokens
token_refresh_schema = swagger_auto_schema(
    operation_description="Refrescar un token JWT con el refresh token",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='Token de refresco'),
        },
        required=['refresh'],
    ),
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'access': openapi.Schema(type=openapi.TYPE_STRING, description='Nuevo token de acceso'),
            },
        ),
        401: "Token de refresco inválido o expirado",
    }
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]