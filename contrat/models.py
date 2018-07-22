# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.core.validators import RegexValidator
from jsonfield import JSONField


class TypeDateDePaiement(models.Model):
    options = models.CharField(max_length=120, blank=True)
    # ((1,1),(2,10),(3,20),(4,30))
    # ((1,1),(10,10),(20,20),(30,30))
    def __unicode__(self):
        return self.options


class TypeModeDePaiement(models.Model):
    options = models.CharField(max_length=240, blank=True)
    # (('CB','CB'),('VIREMENT','VIREMENT'),('CHEQUE','CHEQUE'))
    # (('CB','CB'),('VIREMENT','VIREMENT'))
    def __unicode__(self):
        return self.options


class TypeContrat(models.Model):
    nom = models.CharField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return self.nom


class Produit(models.Model):
    type_contrat = models.ForeignKey(TypeContrat, default='', on_delete=models.CASCADE)
    nom = models.CharField(max_length=120, null=True, blank=True)
    nom_commercial = models.CharField(max_length=120, null=True, blank=True)
    identifiant = models.CharField(max_length=6, null=True, blank=True)
    compagnie_assurance = models.CharField(max_length=120, null=True, blank=True)
    email_compagnie_assurance = models.EmailField()
    branche = models.CharField(max_length=120, null=True, blank=True)
    encaissement = models.CharField(max_length=120, null=True, blank=True)
    profession = JSONField(null=True, blank=True, default='')
    regime = JSONField(null=True, blank=True, default='')

    condition_age_min = models.PositiveIntegerField(null=True, blank=True)
    condition_age_max = models.PositiveIntegerField(null=True, blank=True)
    condition_age_min_conj = models.PositiveIntegerField(null=True, blank=True)
    condition_age_max_conj = models.PositiveIntegerField(null=True, blank=True)
    condition_age_min_enfant = models.PositiveIntegerField(null=True, blank=True)
    condition_age_max_enfant = models.PositiveIntegerField(null=True, blank=True)
    condition_regime = models.CharField(max_length=400, null=True, blank=True)
    condition_code_postal = models.CharField(max_length=400, null=True, blank=True)

    def __unicode__(self):
        return self.nom


class CategorieProduit(models.Model):
    id_produit = models.ForeignKey(Produit, default='', on_delete=models.CASCADE)
    nom = models.CharField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return self.nom


class ZoneProduit(models.Model):
    id_produit = models.ForeignKey(CategorieProduit, default='', on_delete=models.CASCADE)
    numero_zone = models.PositiveSmallIntegerField(null=True, blank=True)
    nom = models.CharField(max_length=120, null=True, blank=True)
    liste_code_postal = models.CharField(max_length=400, null=True, blank=True)
    date_debut = models.DateField(null=True, blank=True)
    date_fin = models.DateField(null=True, blank=True)
    dictionnaire_prix = JSONField(null=True, blank=True, default='')

    def __unicode__(self):
        return "%s - %s" % (self.id_produit, self.nom)


class Contrat(models.Model):
    id = models.AutoField(primary_key=True)
    update_date = models.DateTimeField(auto_now=True)
    civilite = models.CharField(max_length=4, null=True, choices=(('MR', 'M.'), ('MME', 'Mme'), ('MLLE', 'Mlle')))
    nom = models.CharField(max_length=120, null=True, blank=True)
    prenom = models.CharField(max_length=120, null=True, blank=True)
    date_de_naissance = models.DateField(null=True, blank=True)
    regime = models.CharField(max_length=40, null=True, blank=True)
    situation_familliale = models.CharField(max_length=40, null=True, blank=True)
    adresse1 = models.CharField(max_length=120, null=True, blank=True)
    adresse2 = models.CharField(max_length=120, null=True, blank=True)
    code_postal = models.CharField(max_length=5, blank=True, null=True,
                                               validators=[RegexValidator('[0-9]{5}$',
                                                                          """Le numéro doit être du type 01234""")]
                                               )
    ville = models.CharField(max_length=120, null=True, blank=True)
    telephone = models.CharField(max_length=10, blank=True, null=True,
                                  validators=[
                                     RegexValidator('^0[0-9]{9}$', """Le numéro doit être du type 0123456789""")]
                                 )
    email = models.EmailField()
    numero_securite_sociale = models.CharField(max_length=15, blank=True, null=True,
                                               validators=[RegexValidator('^0[0-9]{9}$',
                                                                          """Le numéro doit être du type 0123456789""")]
                                               )
    date_effet = models.DateField(default=timezone.now)

    profession = models.CharField(max_length=120, null=True, blank=True)
    options = models.CharField(max_length=120, null=True, blank=True)
    date_de_paiement = models.PositiveIntegerField(null=True, blank=True)
    mode_de_paiement = models.CharField(max_length=120, null=True, blank=True)
    type_contrat = models.CharField(max_length=120, null=True, blank=True)
    produit = models.CharField(max_length=120, null=True, blank=True)
    type_contrat = models.ForeignKey(TypeContrat, null=True, blank=True, default='', on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, null=True, blank=True, default='', on_delete=models.CASCADE)
    categorie_produit = models.ForeignKey(CategorieProduit, null=True, blank=True, default='', on_delete=models.CASCADE)
    zone_produit = models.ForeignKey(ZoneProduit, null=True, blank=True, default='', on_delete=models.CASCADE)

    def __unicode__(self):
        return "%s %s" % (self.prenom, self.nom)


def get_mode_de_paiement(id1):
    return TypeModeDePaiement.objects.get(id=id1).options


def get_date_de_paiement(id1):
    return TypeDateDePaiement.objects.get(id=id1).options
