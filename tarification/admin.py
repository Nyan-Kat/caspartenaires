# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import contrat
from django.contrib import admin

# Register your models here.


class contratadmin(admin.ModelAdmin):
    class Meta:
        model = contrat

admin.site.register(contrat, contratadmin)
