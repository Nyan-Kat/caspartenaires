# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from contrat.models import *
from django.contrib import admin


# Register your models here.


class contratadmin(admin.ModelAdmin):
    class Meta:
        model = Contrat


admin.site.register(Contrat, contratadmin)
admin.site.register(TypeModeDePaiement, contratadmin)
admin.site.register(TypeDateDePaiement, contratadmin)
admin.site.register(Produit, contratadmin)
admin.site.register(TypeContrat, contratadmin)
admin.site.register(CategorieProduit, contratadmin)
admin.site.register(ZoneProduit, contratadmin)
