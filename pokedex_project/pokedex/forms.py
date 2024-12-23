from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Pokemon, Entrenador
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import json

class CustomUserCreationForm(UserCreationForm):
    equipo = forms.CharField(max_length=100, required=True, help_text='Ingrese el nombre de su equipo.')
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'equipo']

class PokemonForm(forms.ModelForm):
    habilidades = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        required=False  # Campo opcional
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        required=False  # Campo opcional
    )
    tipo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        required=True  # Campo obligatorio
    )
    numero = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        required=True  # Campo obligatorio
    )

    class Meta:
        model = Pokemon
        fields = ['nombre', 'tipo', 'habilidades', 'descripcion', 'altura', 'peso', 
                  'evolucion', 'imagen', 'hp', 'ataque', 'defensa', 'ataque_especial',
                  'defensa_especial', 'velocidad', 'numero']

    def clean_imagen(self):
        imagen = self.cleaned_data['imagen']
        validate = URLValidator()
        try:
            validate(imagen)
        except ValidationError:
            raise ValidationError('La URL de la imagen no es válida.')
        return imagen
    
    def clean_altura(self):
        altura = self.cleaned_data['altura']
        if altura <= 0:
            raise ValidationError('La altura debe ser mayor a 0.')
        return altura
    
    def clean_peso(self):
        peso = self.cleaned_data['peso']
        if peso <= 0:
            raise ValidationError('El peso debe ser mayor a 0.')
        return peso
    
    def clean_hp(self):
        hp = self.cleaned_data['hp']
        if hp <= 0:
            raise ValidationError('Los puntos de vida deben ser mayores a 0.')
        return hp
    
    def clean_ataque(self):
        ataque = self.cleaned_data['ataque']
        if ataque <= 0:
            raise ValidationError('El ataque debe ser mayor a 0.')
        return ataque
    
    def clean_defensa(self):
        defensa = self.cleaned_data['defensa']
        if defensa <= 0:
            raise ValidationError('La defensa debe ser mayor a 0.')
        return defensa
    
    def clean_ataque_especial(self):
        ataque_especial = self.cleaned_data['ataque_especial']
        if ataque_especial <= 0:
            raise ValidationError('El ataque especial debe ser mayor a 0.')
        return ataque_especial
    
    def clean_defensa_especial(self):
        defensa_especial = self.cleaned_data['defensa_especial']
        if defensa_especial <= 0:
            raise ValidationError('La defensa especial debe ser mayor a 0.')
        return defensa_especial
    
    def clean_velocidad(self):
        velocidad = self.cleaned_data['velocidad']
        if velocidad <= 0:
            raise ValidationError('La velocidad debe ser mayor a 0.')
        return velocidad

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ['nombre', 'equipo']

class CapturarPokemonForm(forms.Form):
    pokemon_id = forms.IntegerField(widget=forms.HiddenInput())
    entrenadores = forms.ModelMultipleChoiceField(
        queryset=Entrenador.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['entrenadores'].queryset = Entrenador.objects.filter(user=user)