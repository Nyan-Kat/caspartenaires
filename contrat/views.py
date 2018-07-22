# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, reverse, redirect
from django.http import request, HttpResponse
from django.http.response import HttpResponseRedirect
from django.views.generic import FormView
from contrat.forms import *
import datetime


def home(request, *args, **kwargs):
    return render(request, "home.html")


class CreateContrat1(FormView):
    template_name = 'creer_contrat_step1.html'
    initial = {'nom': 'Cusson', 'prenom': 'Thomas', 'date_de_naissance': datetime.date(1995, 01, 04), 'regime': 'test',
               'email': 'thomas@test.fr', 'telephone': '0123456789', 'date_de_paiement': 10,
               'situation_familliale': 'seul', 'adresse1': 'avenue pierre masse', 'adresse2': 'appartement 735',
               'code_postal': 75014, 'ville': 'Paris'}
    form_model = ContratForm1

    def get(self, request, *args, **kwargs):
        form = self.form_model(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_model(request.POST)
        if form.is_valid():
            form.cleaned_data
            new_contrat = form.save()
            kwargs = {'contrat_id': new_contrat.pk}
            print(str(kwargs))
        # return render(request, "home.html")
        return redirect(reverse('contrat:creercontrat2', kwargs=kwargs))


class CreateContrat2(FormView):
    template_name = 'creer_contrat_step2.html'
    form_model = ContratForm2

    def get(self, request, **kwargs):
        form = self.form_model
        form.id = self.kwargs.get('contrat_id', 4)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        id_contrat = self.form_model(request.POST).id
        print('id = ' + str(id_contrat))
        instance = Contrat.objects.get(pk=id_contrat)
        form = self.form_model(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
        return render(request, "home.html", {'id': id_contrat})



