from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Crée les rôles système (groupes) avec leurs permissions'

    def handle(self, *args, **kwargs):

        # Rôle 1 : Magasinier
        magasinier, created = Group.objects.get_or_create(name='Magasinier')
        if created:
            self.stdout.write(self.style.SUCCESS('✔ Groupe "Magasinier" créé'))
        else:
            self.stdout.write('→ Groupe "Magasinier" existe déjà')

        # Rôle 2 : Responsable Stock
        responsable, created = Group.objects.get_or_create(name='Responsable Stock')
        if created:
            self.stdout.write(self.style.SUCCESS('✔ Groupe "Responsable Stock" créé'))
        else:
            self.stdout.write('→ Groupe "Responsable Stock" existe déjà')

        self.stdout.write(self.style.SUCCESS('\n✅ Rôles système créés avec succès !'))