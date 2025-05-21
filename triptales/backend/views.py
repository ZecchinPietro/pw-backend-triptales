from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class UtenteViewSet(viewsets.ModelViewSet):
    queryset = Utente.objects.all()
    serializer_class = UtenteSerializer
    permission_classes = [IsAuthenticated]

class GruppoViewSet(viewsets.ModelViewSet):
    queryset = Gruppo.objects.all()
    serializer_class = GruppoSerializer
    permission_classes = [IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

class CommentoViewSet(viewsets.ModelViewSet):
    queryset = Commento.objects.all()
    serializer_class = CommentoSerializer
    permission_classes = [IsAuthenticated]
