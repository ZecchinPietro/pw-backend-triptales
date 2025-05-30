CREATE DATABASE pwtriptales_db;
USE pwtriptales_db;

-- Utenti
CREATE TABLE utente (
  id_utente INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  data_registrazione DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Gruppi
CREATE TABLE gruppo (
  id_gruppo INT AUTO_INCREMENT PRIMARY KEY,
  nome_gruppo VARCHAR(100) NOT NULL,
  descrizione VARCHAR(255),
  codice_accesso VARCHAR(50)
);

-- Utenti nei gruppi
CREATE TABLE utente_gruppo (
  id_utente INT,
  id_gruppo INT,
  ruolo VARCHAR(50),
  data_iscrizione DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id_utente, id_gruppo),
  FOREIGN KEY (id_utente) REFERENCES utente(id_utente),
  FOREIGN KEY (id_gruppo) REFERENCES gruppo(id_gruppo)
);

-- Post
CREATE TABLE post (
  id_post INT AUTO_INCREMENT PRIMARY KEY,
  id_utente INT,
  id_gruppo INT,
  titolo VARCHAR(100),
  testo TEXT,
  immagine_path VARCHAR(255),
  data_creazione DATETIME DEFAULT CURRENT_TIMESTAMP,
  latitudine DOUBLE,
  longitudine DOUBLE,
  testo_OCR TEXT,
  testo_tradotto TEXT,
  tags_oggetti VARCHAR(255),
  didascalia_automatica TEXT,
  FOREIGN KEY (id_utente) REFERENCES utente(id_utente),
  FOREIGN KEY (id_gruppo) REFERENCES gruppo(id_gruppo)
);

-- Commenti
CREATE TABLE commento (
  id_commento INT AUTO_INCREMENT PRIMARY KEY,
  id_post INT,
  id_utente INT,
  testo TEXT NOT NULL,
  data_creazione DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_post) REFERENCES post(id_post),
  FOREIGN KEY (id_utente) REFERENCES utente(id_utente)
);

-- Badge
CREATE TABLE badge (
  id_badge INT AUTO_INCREMENT PRIMARY KEY,
  nome_badge VARCHAR(50),
  descrizione VARCHAR(255)
);

-- Badge degli utenti
CREATE TABLE badge_utente (
  id_utente INT,
  id_badge INT,
  data_assegnazione DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id_utente, id_badge),
  FOREIGN KEY (id_utente) REFERENCES utente(id_utente),
  FOREIGN KEY (id_badge) REFERENCES badge(id_badge)
);

-- Like ai post
CREATE TABLE post_like (
  id_like INT AUTO_INCREMENT PRIMARY KEY,
  id_utente_che_ha_messo_like INT,
  id_post INT,
  data_like DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_utente_che_ha_messo_like) REFERENCES utente(id_utente),
  FOREIGN KEY (id_post) REFERENCES post(id_post)
);