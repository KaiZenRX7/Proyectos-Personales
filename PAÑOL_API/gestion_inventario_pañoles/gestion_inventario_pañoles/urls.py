"""
URL configuration for gestion_inventario_pañoles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from .swagger import schema_view
from gestion_activos.auth import urlpatterns as auth_urls
from gestion_activos.views import home, activos_list


urlpatterns = [
    path('admin/', admin.site.urls , name='admin_login'),
    path('admin/logout/', LogoutView.as_view(), name='admin_logout'),
    
    # Ruta de la pagina principal
    path('', home, name='home'),
    path('activos/', activos_list, name='activos_list'),

    # Rutas de la aplicacion gestion_activos
    path('api/', include('gestion_activos.urls')),


    # Rutas de autenticacion
    path('api/auth/', include(auth_urls)),
    # Documentacion Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
