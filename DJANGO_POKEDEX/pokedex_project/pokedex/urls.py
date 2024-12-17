from django.urls import path
from . import views

urlpatterns = [
    path('pokemons/', views.PokemonListView.as_view(), name='lista_pokemon'),
    path('entrenadores/', views.TrainerListView.as_view(), name='entrenadores'),
    path('crear_entrenador/', views.EntrenadorCreateView.as_view(), name='crear_entrenador'),
    path('eliminar_entrenador/<int:pk>/', views.EntrenadorDeleteView.as_view(), name='eliminar_entrenador'),
    path('perfil/', views.ProfileView.as_view(), name='perfil'),
    path('buscar/', views.PokemonSearchView.as_view(), name='buscar_pokemon'),
    path('pokemons/<int:pk>/', views.PokemonDetailView.as_view(), name='detalles_pokemon'),
    path('pokemons/<int:pk>/editar/', views.PokemonUpdateView.as_view(), name='editar_pokemon'),
    path('pokemons/<int:pk>/eliminar/', views.PokemonDeleteView.as_view(), name='eliminar_pokemon'),
    path('retirar_pokemon/<int:pk>/', views.retirar_pokemon, name='retirar_pokemon'),
    path('api/entrenadores/', views.obtener_entrenadores, name='obtener_entrenadores'),
]