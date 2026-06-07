from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('produits/', views.produit_liste, name='produit_liste'),
    path('produits/<int:pk>/', views.produit_detail, name='produit_detail'),
    path('produits/ajouter/', views.produit_ajouter, name='produit_ajouter'),
    path('produits/<int:pk>/modifier/', views.produit_modifier, name='produit_modifier'),
    path('produits/<int:pk>/supprimer/', views.produit_supprimer, name='produit_supprimer'),
    path('fournisseurs/', views.fournisseur_liste, name='fournisseur_liste'),
    path('fournisseurs/ajouter/', views.fournisseur_ajouter, name='fournisseur_ajouter'),
    path('fournisseurs/<int:pk>/modifier/', views.fournisseur_modifier, name='fournisseur_modifier'),
    path('mouvements/', views.mouvement_liste, name='mouvement_liste'),
    path('mouvements/ajouter/', views.mouvement_ajouter, name='mouvement_ajouter'),
]