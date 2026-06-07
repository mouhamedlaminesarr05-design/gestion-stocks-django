from django.contrib import admin
from .models import Categorie, Fournisseur, Produit, MouvementStock


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom']
    search_fields = ['nom']


@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email', 'telephone']
    search_fields = ['nom', 'email']


@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'reference', 'prix', 'quantite_stock', 'seuil_alerte', 'categorie', 'fournisseur']
    search_fields = ['nom', 'reference']
    list_filter = ['categorie', 'fournisseur']


@admin.register(MouvementStock)
class MouvementStockAdmin(admin.ModelAdmin):
    list_display = ['produit', 'type_mouvement', 'quantite', 'date', 'effectue_par']
    list_filter = ['type_mouvement']