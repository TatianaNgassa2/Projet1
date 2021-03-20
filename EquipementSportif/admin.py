from django.contrib import admin

# Register your models here.
from EquipementSportif.models import *

admin.site.register(Equipement)
admin.site.register(Stock)
admin.site.register(LigneActivite)
admin.site.register(Etablissement)
admin.site.register(Etudiant)