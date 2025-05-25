from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UtenteViewSet, GruppoViewSet, PostViewSet, CommentoViewSet

router = DefaultRouter()
router.register(r'utenti', UtenteViewSet)
router.register(r'gruppi', GruppoViewSet)
router.register(r'posts', PostViewSet)
router.register(r'commenti', CommentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
