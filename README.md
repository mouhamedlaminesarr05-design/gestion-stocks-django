 📦 Gestion des Stocks — Django

Application web de gestion des stocks pour PME développée avec Django et MySQL.

## 🎯 Objectif
Gérer les entrées et sorties de produits, les fournisseurs, et les mouvements de stock pour une PME du secteur sportif.

## ✅ Fonctionnalités
- Authentification complète (inscription, connexion, déconnexion, changement de mot de passe)
- Email comme identifiant principal
- Gestion des rôles (Magasinier, Responsable Stock)
- Profil utilisateur modifiable avec photo de profil
- CRUD complet Produits, Fournisseurs, Catégories
- Historique des mouvements de stock (entrées/sorties)
- Alertes automatiques si stock en dessous du seuil
- Tableau de bord avec statistiques
- Pagination sur toutes les listes
- Interface responsive Bootstrap 5

## 👥 Rôles

| Rôle | Permissions |
|------|-------------|
| Magasinier | Consulter les produits + enregistrer les mouvements de stock |
| Responsable Stock | Gérer produits, fournisseurs, catégories et mouvements |
| Admin | Accès total à toute l'application |

## 🛠️ Technologies utilisées

| Technologie | Version |
|-------------|---------|
| Python | 3.12 |
| Django | 4.2 |
| MySQL / MariaDB | 10.4+ |
| Bootstrap | 5.3 |
| Pillow | dernière version |

## 📁 Structure du projet
gestion_stocks/
│
├── core/                  ← Configuration globale
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── accounts/              ← Authentification & Profils
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── decorators.py
│   └── templates/
│
├── stocks/                ← Gestion des stocks
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── templates/             ← Templates globaux
├── manage.py
├── requirements.txt
└── README.md

## ⚙️ Installation

### 1. Cloner le projet
git clone https://github.com/tonnom/gestion-stocks-django.git
cd gestion-stocks-django

### 2. Créer l'environnement virtuel
python -m venv env
env\Scripts\activate

### 3. Installer les dépendances
pip install -r requirements.txt

### 4. Configurer la base de données
Créer une base de données MySQL nommée `gestion_stocks_db` et modifier `core/settings.py` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gestion_stocks_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Lancer les migrations
python manage.py migrate

### 6. Créer les rôles système
python manage.py createsystemroles

### 7. Créer un super utilisateur
python manage.py createsuperuser

### 8. Lancer le serveur
python manage.py runserver

### 9. Accéder à l'application
- Site : http://127.0.0.1:8000/stocks/
- Admin : http://127.0.0.1:8000/admin/

## 📸 Pages de l'application

| Page | URL |
|------|-----|
| Tableau de bord | /stocks/ |
| Liste des produits | /stocks/produits/ |
| Liste des fournisseurs | /stocks/fournisseurs/ |
| Mouvements de stock | /stocks/mouvements/ |
| Connexion | /accounts/login/ |
| Inscription | /accounts/register/ |
| Profil | /accounts/profile/ |
| Admin | /admin/ |

## 👨‍💻 Auteur
Projet réalisé dans le cadre du CCP 2026 — Framework Django