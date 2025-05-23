from rest_framework import serializers
from .models import *

class UtenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utente
        fields = ['id', 'nome', 'email', 'password_hash', 'data_registrazione']

class GruppoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gruppo
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commento
        fields = '__all__'
