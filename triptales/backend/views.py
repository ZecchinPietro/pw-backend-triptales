from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Utente, Gruppo, Post, Commento
from .serializers import (
    UtenteSerializer, GruppoSerializer, PostSerializer,
    CommentoSerializer, MyTokenObtainPairSerializer
)

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

@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    data = request.data
    email = data.get('email')
    nome = data.get('nome')
    password = data.get('password')

    if not email or not nome or not password:
        return Response({'error': 'Campi mancanti'}, status=status.HTTP_400_BAD_REQUEST)

    if Utente.objects.filter(email=email).exists():
        return Response({'error': 'Utente già esistente'}, status=status.HTTP_400_BAD_REQUEST)

    utente = Utente(
        email=email,
        nome=nome,
        password=make_password(password)
    )
    utente.save()
    return Response({'message': 'Registrazione completata'}, status=status.HTTP_201_CREATED)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
