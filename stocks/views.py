from accounts.decorators import role_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Produit, Fournisseur, Categorie, MouvementStock
from .forms import ProduitForm, FournisseurForm, CategorieForm, MouvementStockForm


# ─── TABLEAU DE BORD ────────────────────────────────────────────
@login_required
def dashboard(request):
    produits = Produit.objects.all()
    alertes = [p for p in produits if p.est_en_alerte()]
    total_produits = produits.count()
    total_fournisseurs = Fournisseur.objects.count()
    derniers_mouvements = MouvementStock.objects.all()[:5]
    return render(request, 'stocks/dashboard.html', {
        'alertes': alertes,
        'total_produits': total_produits,
        'total_fournisseurs': total_fournisseurs,
        'derniers_mouvements': derniers_mouvements,
    })


# ─── PRODUITS ───────────────────────────────────────────────────
@login_required
@role_required('Magasinier', 'Responsable Stock')
def produit_liste(request):
    produits = Produit.objects.all()
    paginator = Paginator(produits, 10)  # 10 produits par page
    page = request.GET.get('page')
    produits = paginator.get_page(page)
    return render(request, 'stocks/produit_liste.html', {'produits': produits})


@login_required
@role_required('Magasinier', 'Responsable Stock')
def produit_detail(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    mouvements = produit.mouvements.all()[:10]
    return render(request, 'stocks/produit_detail.html', {
        'produit': produit,
        'mouvements': mouvements,
    })


@login_required
@role_required('Magasinier', 'Responsable Stock')
def produit_ajouter(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit ajouté avec succès !')
            return redirect('produit_liste')
    else:
        form = ProduitForm()
    return render(request, 'stocks/produit_form.html', {'form': form, 'titre': 'Ajouter un produit'})


@login_required
@role_required('Responsable Stock')
def produit_modifier(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit modifié avec succès !')
            return redirect('produit_liste')
    else:
        form = ProduitForm(instance=produit)
    return render(request, 'stocks/produit_form.html', {'form': form, 'titre': 'Modifier un produit'})


@login_required
@role_required('Responsable Stock')
def produit_supprimer(request, pk):
    produit = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        produit.delete()
        messages.success(request, 'Produit supprimé !')
        return redirect('produit_liste')
    return render(request, 'stocks/produit_confirmer_suppression.html', {'produit': produit})


# ─── FOURNISSEURS ────────────────────────────────────────────────
@login_required
@role_required('Responsable Stock')
def fournisseur_liste(request):
    fournisseurs = Fournisseur.objects.all()
    paginator = Paginator(fournisseurs, 10)
    page = request.GET.get('page')
    fournisseurs = paginator.get_page(page)
    return render(request, 'stocks/fournisseur_liste.html', {'fournisseurs': fournisseurs})


@login_required
@role_required('Responsable Stock')
def fournisseur_ajouter(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fournisseur ajouté avec succès !')
            return redirect('fournisseur_liste')
    else:
        form = FournisseurForm()
    return render(request, 'stocks/fournisseur_form.html', {'form': form, 'titre': 'Ajouter un fournisseur'})


@login_required
@role_required('Responsable Stock')
def fournisseur_modifier(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fournisseur modifié avec succès !')
            return redirect('fournisseur_liste')
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'stocks/fournisseur_form.html', {'form': form, 'titre': 'Modifier un fournisseur'})


# ─── MOUVEMENTS DE STOCK ─────────────────────────────────────────
@login_required
@role_required('Magasinier', 'Responsable Stock')
def mouvement_liste(request):
    mouvements = MouvementStock.objects.all()
    paginator = Paginator(mouvements, 10)
    page = request.GET.get('page')
    mouvements = paginator.get_page(page)
    return render(request, 'stocks/mouvement_liste.html', {'mouvements': mouvements})


@login_required
@role_required('Magasinier', 'Responsable Stock')
def mouvement_ajouter(request):
    if request.method == 'POST':
        form = MouvementStockForm(request.POST)
        if form.is_valid():
            mouvement = form.save(commit=False)
            mouvement.effectue_par = request.user
            # Mettre à jour la quantité du produit
            produit = mouvement.produit
            if mouvement.type_mouvement == 'entree':
                produit.quantite_stock += mouvement.quantite
            else:
                produit.quantite_stock -= mouvement.quantite
            produit.save()
            mouvement.save()
            messages.success(request, 'Mouvement enregistré avec succès !')
            return redirect('mouvement_liste')
    else:
        form = MouvementStockForm()
    return render(request, 'stocks/mouvement_form.html', {'form': form, 'titre': 'Nouveau mouvement'})