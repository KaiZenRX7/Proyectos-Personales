from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from pokedex import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='inicio_sesion'),
    path('cerrar_sesion/', views.custom_logout_view, name='cerrar_sesion'),
    path('registro/', views.register, name='registro'),
    path('pokedex/', include('pokedex.urls')),  # Incluir las URLs de la aplicación pokedex
]