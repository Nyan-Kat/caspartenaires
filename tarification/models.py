# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.utils.encoding import smart_unicode
from django.db import models


# Create your models here.

class contrat(models.Model):
    update_date = models.DateTimeField(auto_now=True)
    civilite = models.CharField(max_length=4, null=False, choices=(('Monsieur', 'M.'), ('Madame', 'Mme'), ('Mademoiselle', 'Mlle')))
    nom = models.CharField(max_length=120, null=True, blank=True)
    prenom = models.CharField(max_length=120, null=True, blank=True)
    date_de_naissance = models.DateField(null=True, blank=True)
    regime = models.CharField(max_length=40, null=True, blank=True)
    situation_familliale = models.CharField(max_length=40, null=True, blank=True)
    adresse1 = models.CharField(max_length=120, null=True, blank=True)
    adresse2 = models.CharField(max_length=120, null=True, blank=True)
    code_postal = models.PositiveIntegerField(null=True, blank=True)
    ville = models.CharField(max_length=120, null=True, blank=True)
    telephone = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField()
    numero_securite_sociale = models.CharField(max_length=15, null=True, blank=True)
    date_effet = models.DateField(default=timezone.now)

    def __unicode__(self):
        return smart_unicode(self.prenom &" "& self.nom)
