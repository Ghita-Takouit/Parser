# Analyseur de Phrase Française

Un analyseur syntaxique simple pour des phrases françaises basiques suivant la structure Sujet-Verbe-Complément.

## Description

Ce projet implémente un analyseur de phrases françaises qui vérifie si une phrase suit la structure grammaticale:
- Article + Nom (Sujet)
- Verbe
- Article + Nom (Complément)

## Installation

1. Cloner le repository
2. Installer les dépendances:
```bash
pip install -r requirements.txt
```

## Utilisation

1. Lancer l'application:
```bash
python app.py
```

2. Ouvrir un navigateur et accéder à `http://localhost:5001`

3. Entrer une phrase à analyser dans le format:
   - Exemple valide: "Le chat mange la souris"
   - Exemple valide: "La voiture traverse la ville"

## Fonctionnalités

- Interface web interactive
- Validation en temps réel
- Historique des phrases analysées
- Retour visuel sur la validité de la phrase
- Support pour un vocabulaire prédéfini de:
  - Articles (le, la, les, etc.)
  - Noms (chat, souris, maison, etc.)
  - Verbes (mange, voit, traverse, etc.)

## Technologies Utilisées

- Flask (Backend)
- HTML/CSS avec Tailwind CSS
- JavaScript pour les interactions frontend
