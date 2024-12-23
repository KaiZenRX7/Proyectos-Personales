from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Activo
from .serializers import ActivoSerializer
from rest_framework.permissions import IsAuthenticated
from .http_errors import handle_http_error

# Create your views here.

class ActivoViewSet(ModelViewSet):
    queryset = Activo.objects.all()
    serializer_class = ActivoSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as e:
            return handle_http_error(400)

    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Exception as e:
            return handle_http_error(400)

    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Exception as e:
            return handle_http_error(400)

def home(request):
    return render(request, 'home_api.html')

def activos_list(request):
    try:
        activos = Activo.objects.all()
        return render(request, 'activos_list.html', {'activos': activos})
    except Exception as e:
        return handle_http_error(500)