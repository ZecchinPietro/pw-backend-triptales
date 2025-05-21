from django.db import models
from django.contrib.auth.models import AbstractUser

class Utente(AbstractUser):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_registrazione = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class Gruppo(models.Model):
    nome_gruppo = models.CharField(max_length=100)
    descrizione = models.CharField(max_length=255, blank=True)
    codice_accesso = models.CharField(max_length=50, blank=True)

class UtenteGruppo(models.Model):
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    ruolo = models.CharField(max_length=50, default='partecipante')
    data_iscrizione = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    gruppo = models.ForeignKey(Gruppo, on_delete=models.CASCADE)
    titolo = models.CharField(max_length=100)
    testo = models.TextField(blank=True)
    immagine_path = models.ImageField(upload_to='foto_post/')
    data_creazione = models.DateTimeField(auto_now_add=True)
    latitudine = models.FloatField(null=True, blank=True)
    longitudine = models.FloatField(null=True, blank=True)
    testo_OCR = models.TextField(blank=True, null=True)
    testo_tradotto = models.TextField(blank=True, null=True)
    tags_oggetti = models.CharField(max_length=255, blank=True, null=True)
    didascalia_automatica = models.TextField(blank=True, null=True)

class Commento(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    testo = models.TextField()
    data_creazione = models.DateTimeField(auto_now_add=True)

class Badge(models.Model):
    nome_badge = models.CharField(max_length=50)
    descrizione = models.CharField(max_length=255)

class BadgeUtente(models.Model):
    utente = models.ForeignKey(Utente, on_delete=models.CASCADE)
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    data_assegnazione = models.DateTimeField(auto_now_add=True)

class PostLike(models.Model):
    utente_che_ha_messo_like = models.ForeignKey(Utente, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_like = models.DateTimeField(auto_now_add=True)
