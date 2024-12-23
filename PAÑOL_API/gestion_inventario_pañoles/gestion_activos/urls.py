from rest_framework.routers import DefaultRouter
from.views import ActivoViewSet, home
from django.urls import path

router = DefaultRouter()
router.register(r'activos', ActivoViewSet)



urlpatterns = router.urls

