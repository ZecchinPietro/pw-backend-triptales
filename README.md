# TripTales – Backend (Django + MySQL)

Questo repository contiene il **backend del progetto TripTales – Diario di Gita con Intelligenza Artificiale**, sviluppato con **Django REST Framework** e connesso a un database **MySQL** via **XAMPP**.

Il backend gestisce autenticazione utenti (JWT), gruppi di gita, post collaborativi, commenti, badge, e supporta la ricezione di metadati ML Kit (OCR, oggetti, traduzioni, ecc.) dal frontend Android.

---

## ⚙️ Requisiti

- Python 3.x
- pip
- MySQL (XAMPP attivo su `localhost`)
- Librerie Python:
  - Django
  - djangorestframework
  - djangorestframework-simplejwt
  - mysqlclient

---

## 📦 Installazione

1. Clona il repository:
   ```bash
   git clone https://github.com/tuo-utente/pw-backend-triptales.git
   cd pw-backend-triptales

    Crea e attiva un ambiente virtuale:

python -m venv venv
source venv/bin/activate  # Su Windows: .\venv\Scripts\activate

Installa le dipendenze:

pip install -r requirements.txt

Configura il database MySQL in triptales/settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'pwtriptales_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Esegui le migrazioni:

python manage.py makemigrations
python manage.py migrate

Avvia il server:

    python manage.py runserver

🔐 Autenticazione JWT

Il backend utilizza JWT (JSON Web Token) tramite djangorestframework-simplejwt.
API disponibili:

    POST /api/accounts/register/ – Registrazione utente

    POST /api/accounts/login/ – Login (ritorna access e refresh token)

    Per chiamate protette, invia l'header:

Authorization: Bearer <access_token>

🧩 Funzionalità implementate

    ✅ Autenticazione e registrazione utenti (JWT)

    ✅ Creazione e gestione gruppi gita

    ✅ Post con immagini, descrizioni e metadati ML Kit (OCR, oggetti, ecc.)

    ✅ Commenti tra utenti

    ✅ Badge per attività (Esploratore, Traduttore, Osservatore)

    ✅ Classifica utenti attivi

    ✅ API REST integrate con Android (Retrofit)

🧪 Test con Postman

Esegui il backend con runserver, poi prova queste chiamate in Postman:

    Registrazione:

        POST http://localhost:8000/api/accounts/register/

        Body (JSON):

    {
      "username": "mario",
      "email": "mario@email.com",
      "password": "12345678"
    }

Login:

    POST http://localhost:8000/api/accounts/login/

    Body (JSON):

    {
      "username": "mario",
      "password": "12345678"
    }

Accesso ad API protette:

    Aggiungi il token JWT nei headers:

        Authorization: Bearer <access_token>

📂 Struttura progetto

pw-backend-triptales/
├── manage.py
├── triptales/          # Configurazione Django
│   ├── settings.py
│   └── urls.py
├── accounts/           # Autenticazione e utenti (JWT)
├── groups/             # (Facoltativo) gestione gruppi
├── posts/              # (Facoltativo) diario, immagini, commenti
└── requirements.txt

🛠 Strumenti usati

    Django REST Framework

    JWT (SimpleJWT)

    MySQL via XAMPP

    Postman (test API)

    Firebase ML Kit (gestito lato frontend)

🔗 Frontend collegato

Il frontend Android è disponibile nella repo pw-frontend-triptales, e comunica con il backend via Retrofit.

Uso didattico – Istituto Tecnico Informatico ITIS ROSSI Quinta Superiore.

Crediti: Favero Mattia, Minante Davide, Zecchin Pietro



