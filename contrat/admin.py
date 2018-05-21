# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from contrat.models import *
from django.contrib import admin


# Register your models here.


class contratadmin(admin.ModelAdmin):
    class Meta:
        model = contrat


admin.site.register(contrat, contratadmin)
admin.site.register(type_mode_de_paiement, contratadmin)
admin.site.register(type_date_de_paiement, contratadmin)
