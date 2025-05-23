from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('utenti', UtenteViewSet)
router.register('gruppi', GruppoViewSet)
router.register('posts', PostViewSet)
router.register('commenti', CommentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
