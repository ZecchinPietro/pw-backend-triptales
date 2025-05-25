from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Gruppo, Post, Commento

User = get_user_model()

class UtenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome', 'email', 'date_joined']

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

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        attrs['username'] = attrs.get('email')
        return super().validate(attrs)
