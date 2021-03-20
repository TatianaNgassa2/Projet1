from django.db import models

# Create your models here.

class Etablissement(models.Model):
    code = models.CharField (max_length = 80,primary_key=True)
    intitule = models.CharField (max_length = 80)
    ville = models.CharField (max_length = 80)
    region = models.CharField (max_length = 80)
    #age = models.IntegerField ()
    
    def __str__(self):
        return self.code

class Etudiant(models.Model):
    matricule=models.CharField (max_length =255,primary_key=True)
    nom = models.CharField (max_length = 80)
    premon= models.CharField (max_length = 80)
    email= models.EmailField(max_length = 80)
    #etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    def __str__(self):
        return self.matricule

class Equipement(models.Model):
    code = models.CharField (max_length = 80,primary_key=True)
    intitule = models.CharField (max_length = 80)

    def __str__(self):
        return self.code


class Stock(models.Model):
    equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    Etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE)
    quantite = models.IntegerField ()

    def __str__(self):
        return self.quantite
    
class Activite(models.Model):
    #name = models.CharField (max_length = 80)
    type = models.IntegerField (null=False)
    date_creation=models.DateTimeField(auto_now_add=True, auto_now=False)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return self.type

class LigneActivite(models.Model):
    Activite = models.ForeignKey(Activite, on_delete=models.CASCADE)
    Equipement = models.ForeignKey(Equipement, on_delete=models.CASCADE)
    quantite = models.IntegerField ()
    date_debut_emprunt=models.DateTimeField(auto_now_add=True, auto_now=False)
    date_fin_emprunt=models.DateTimeField(auto_now_add=True, auto_now=False)
    date_restitution=models.DateTimeField(auto_now_add=True, auto_now=False)
    statut= models.IntegerField ()

    def __str__(self):
        return self.statut
    
