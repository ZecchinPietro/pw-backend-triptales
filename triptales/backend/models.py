from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class UtenteManager(BaseUserManager):
    def create_user(self, email, nome, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'email è obbligatoria')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, nome, password, **extra_fields)

class Utente(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    objects = UtenteManager()

    def __str__(self):
        return self.email


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
