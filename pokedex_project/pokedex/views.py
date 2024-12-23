import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView, UpdateView, DeleteView, CreateView, FormView
from django.views import View
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import Pokemon, Entrenador
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate, update_session_auth_hash, logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from .forms import CustomUserCreationForm, EntrenadorForm ,CapturarPokemonForm, PokemonForm
from django.db import models

@method_decorator(login_required, name='dispatch')
class PokemonListView(ListView):
    model = Pokemon
    template_name = 'pokedex/lista_pokemon.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                models.Q(nombre__icontains=query) |
                models.Q(tipo__icontains=query)
            )
        return queryset

    def post(self, request, *args, **kwargs):
        form = CapturarPokemonForm(request.POST, user=request.user)
        if form.is_valid():
            pokemon_id = form.cleaned_data['pokemon_id']
            entrenadores = form.cleaned_data['entrenadores']
            pokemon = get_object_or_404(Pokemon, id=pokemon_id)
            for entrenador in entrenadores:
                if entrenador.can_add_pokemon():
                    entrenador.pokemons.add(pokemon)
                    messages.success(request, f'{pokemon.nombre} ha sido añadido al equipo de {entrenador.nombre}.')
                else:
                    messages.error(request, f'{entrenador.nombre} no puede añadir más de 6 Pokémon a su equipo.')
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    


@method_decorator(login_required, name='dispatch')
class TrainerListView(ListView):
    model = Entrenador
    template_name = 'pokedex/entrenadores.html'
    context_object_name = 'object_list'

@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
    template_name = 'pokedex/perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['entrenadores'] = Entrenador.objects.filter(user=self.request.user)
        return context
    

@method_decorator(login_required, name='dispatch')
class PokemonDetailView(DetailView):
    model = Pokemon
    template_name = 'pokedex/detalles_pokemon.html'
    context_object_name = 'pokemon'


@method_decorator(login_required, name='dispatch')
class PokemonSearchView(View):
    def get(self, request):
        return render(request, 'pokedex/buscar_pokemon.html')
    
    def post(self, request):
        name = request.POST.get('name')
        if not name:
            return render(request, 'pokedex/buscar_pokemon.html', {'error': 'Por favor, ingresa el nombre de un Pokémon.'})
        
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name.lower()}')
        if response.status_code == 200:
            data = response.json()
            try:
                # Verificar si el Pokémon ya existe en la base de datos
                if Pokemon.objects.filter(nombre=data['name']).exists():
                    return render(request, 'pokedex/buscar_pokemon.html', {'error': 'Este Pokémon ya está en la lista.'})

                species_url = data['species']['url']
                species_response = requests.get(species_url)
                if species_response.status_code == 200:
                    species_data = species_response.json()
                    evolution_chain_url = species_data.get('evolution_chain', {}).get('url', '')

                    # Obtener la descripción en español (o inglés si no está disponible en español)
                    flavor_text_entries = species_data.get('flavor_text_entries', [])
                    descripcion = next((entry['flavor_text'] for entry in flavor_text_entries if entry['language']['name'] == 'es'), None)
                    if not descripcion:
                        descripcion = next((entry['flavor_text'] for entry in flavor_text_entries if entry['language']['name'] == 'en'), '')

                    # Obtener los nombres de las evoluciones
                    evoluciones = []
                    if evolution_chain_url:
                        evolution_chain_response = requests.get(evolution_chain_url)
                        if evolution_chain_response.status_code == 200:
                            evolution_chain_data = evolution_chain_response.json()
                            chain = evolution_chain_data.get('chain', {})
                            while chain:
                                evoluciones.append(chain['species']['name'])
                                if chain['evolves_to']:
                                    chain = chain['evolves_to'][0]
                                else:
                                    chain = None
                    evoluciones_str = ', '.join(evoluciones)

                else:
                    evolution_chain_url = ''
                    descripcion = ''
                    evoluciones_str = ''
                
                # Obtener la URL de la imagen
                imagen_url = data['sprites']['other']['official-artwork'].get('front_default')
                if not imagen_url:
                    imagen_url = data['sprites'].get('front_default')

                # Obtener las habilidades
                habilidades = {ability['ability']['name']: ability['is_hidden'] for ability in data['abilities']}

                # Obtener los tipos
                tipos = [tipo['type']['name'] for tipo in data['types']]

                # Convierte la altura y el peso de decímetros a metros y hectogramos a kilogramos
                altura = data['height'] / 10
                peso = data['weight'] / 10

                hp = data['stats'][0]['base_stat']
                ataque = data['stats'][1]['base_stat']
                defensa = data['stats'][2]['base_stat']
                ataque_especial = data['stats'][3]['base_stat']
                defensa_especial = data['stats'][4]['base_stat']
                velocidad = data['stats'][5]['base_stat']
                numero = data['id']

                pokemon = Pokemon.objects.create(
                    nombre=data['name'],
                    tipo=tipos,
                    habilidades=habilidades,
                    descripcion=descripcion,
                    altura=altura,
                    peso=peso,
                    evolucion=evoluciones_str,
                    imagen=imagen_url,
                    hp=hp,
                    ataque=ataque,
                    defensa=defensa,
                    ataque_especial=ataque_especial,
                    defensa_especial=defensa_especial,
                    velocidad=velocidad,
                    numero=numero
                )
                return redirect('lista_pokemon')
            except KeyError:
                return render(request, 'pokedex/buscar_pokemon.html', {'error': 'Error al procesar los datos del Pokémon.'})
        else:
            return render(request, 'pokedex/buscar_pokemon.html', {'error': 'Pokémon no encontrado.'})

@method_decorator(login_required, name='dispatch')
class PokemonUpdateView(UpdateView):
    model = Pokemon
    form_class = PokemonForm
    template_name = 'pokedex/actualizar_pokemon.html'
    success_url = reverse_lazy('lista_pokemon')

    def get_initial(self):
        """
        Prepara los valores iniciales para el formulario.
        """
        initial = super().get_initial()
        habilidades = self.object.habilidades
        if habilidades:
            habilidades_list = [
                f"{key} (oculta)" if value else key
                for key, value in habilidades.items()
            ]
            initial['habilidades'] = "\n".join(habilidades_list)
        initial['tipo'] = ", ".join(self.object.tipo)  # Mostrar los tipos separados por comas
        return initial

    def form_valid(self, form):
        """
        Procesa y convierte las habilidades de texto a JSON.
        """
        habilidades = form.cleaned_data['habilidades']
        if habilidades:
            habilidades_list = habilidades.split("\n")
            habilidades_json = {
                habilidad.replace(" (oculta)", "").strip(): "(oculta)" in habilidad
                for habilidad in habilidades_list
            }
            form.instance.habilidades = habilidades_json
        else:
            form.instance.habilidades = None  # Asegurarse de que no haya valores vacíos.
        form.instance.tipo = [t.strip() for t in form.cleaned_data['tipo'].split(",")]  # Convertir a lista de cadenas
        form.save()
        return JsonResponse({'success': True, 'redirect_url': str(self.success_url)})

    def form_invalid(self, form):
        # Si la solicitud es AJAX, devuelve errores de validación en JSON
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            errors = {field: error.get_json_data() for field, error in form.errors.items()}
            return JsonResponse({'success': False, 'errors': errors}, status=400)

        return super().form_invalid(form)
    

@method_decorator(login_required, name='dispatch')
class PokemonDeleteView(DeleteView):
    model = Pokemon
    template_name = 'pokedex/eliminar_pokemon.html'
    success_url = reverse_lazy('lista_pokemon')


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            equipo = form.cleaned_data.get('equipo')
            Entrenador.objects.create(user=user, nombre=user.username, equipo=equipo)
            auth_login(request, user)
            return HttpResponseRedirect(reverse('inicio_sesion') + '?success=1')
        else:
            return render(request, 'autenticacion/registro.html', {'form': form, 'error': 'Hubo un error en el registro. Por favor, revisa los campos.'})
    else:
        form = CustomUserCreationForm()
        return render(request, 'autenticacion/registro.html', {'form': form})

def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse('buscar_pokemon') + '?login_success=1')
        else:
            # Define un mensaje de error en el contexto
            context['error_message'] = 'Usuario o contraseña incorrectos.'
    return render(request, 'autenticacion/inicio_sesion.html', context)


def custom_logout_view(request):
    username = request.user.username
    logout(request)
    return HttpResponseRedirect(reverse('inicio_sesion') + f'?logout_success=1&username={username}')


@login_required
def retirar_pokemon(request, pk):
    pokemon = get_object_or_404(Pokemon, pk=pk)
    entrenador = request.user.entrenador_set.first()
    if entrenador and pokemon in entrenador.pokemons.all():
        entrenador.pokemons.remove(pokemon)
        messages.success(request, f'{pokemon.nombre} ha sido retirado de tu equipo.')
    else:
        messages.error(request, f'{pokemon.nombre} no está en tu equipo.')
    return redirect('perfil')


@method_decorator(login_required, name='dispatch')
class EntrenadorCreateView(CreateView):
    model = Entrenador
    form_class = EntrenadorForm
    template_name = 'pokedex/crear_entrenador.html'
    success_url = reverse_lazy('entrenadores')

    def form_valid(self, form):
        form.instance.user = self.request.user if self.request.user.is_authenticated else None
        form.instance.es_ficticio = True
        response = super().form_valid(form)
        self.request.session['entrenador_id'] = self.object.id
        return response
    

@method_decorator(login_required, name='dispatch')
class EntrenadorDeleteView(DeleteView):
    model = Entrenador
    template_name = 'pokedex/entrenador_confirm_delete.html'
    success_url = reverse_lazy('entrenadores')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user and self.object.user == request.user:
            messages.error(request, 'No puedes eliminar tu propio usuario.')
        elif self.object.user is None:
            self.object.delete()
            messages.success(request, f'Entrenador {self.object.nombre} ha sido eliminado.')
        else:
            messages.error(request, 'No tienes permiso para eliminar este entrenador.')
        return redirect(self.success_url)
    

@login_required
def obtener_entrenadores(request):
    entrenadores = Entrenador.objects.filter(user=request.user)
    data = {
        'entrenadores': [
            {
                'id': entrenador.id,
                'nombre': entrenador.nombre,
                'pokemons': list(entrenador.pokemons.values('id', 'nombre'))
            }
            for entrenador in entrenadores
        ]
    }
    return JsonResponse(data)

