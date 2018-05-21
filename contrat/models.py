# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.core.validators import RegexValidator


class type_date_de_paiement(models.Model):
    options = models.CharField(max_length=120, blank=True)


class type_mode_de_paiement(models.Model):
    options = models.CharField(max_length=240, blank=True)


def get_mode_de_paiement(id1):
    return type_mode_de_paiement.objects.get(id=id1).options


def get_date_de_paiement(id1):
    return type_date_de_paiement.objects.get(id=id1).options


class contrat(models.Model):
    update_date = models.DateTimeField(auto_now=True)
    civilite = models.CharField(max_length=4, null=False, choices=(('MR', 'M.'), ('MME', 'Mme'), ('MLLE', 'Mlle')))
    nom = models.CharField(max_length=120, null=True, blank=True)
    prenom = models.CharField(max_length=120, null=True, blank=True)
    date_de_naissance = models.DateField(null=True, blank=True)
    regime = models.CharField(max_length=40, null=True, blank=True)
    situation_familliale = models.CharField(max_length=40, null=True, blank=True)
    adresse1 = models.CharField(max_length=120, null=True, blank=True)
    adresse2 = models.CharField(max_length=120, null=True, blank=True)
    code_postal = models.PositiveIntegerField(null=True, blank=True)
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
