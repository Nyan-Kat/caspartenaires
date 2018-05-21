# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.generic import FormView
from contrat.forms import *

# Create your views here.
def home(request):
    return render(request, "home.html")


class CreateContrat(FormView):

    template_name = 'creer_contrat.html'

    def get(self, request, *args, **kwargs):
        form_contrat = Contratform()
        return render(request, self.template_name, {'form': form_contrat})

    def post(self, request, *args, **kwargs):
        form = Contratform(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            # return redirect('home')

        args = {'form': form}
        return render(request, self.template_name, args)


