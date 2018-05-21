from django import forms
from contrat.models import *
# from django.forms import ModelForm, DateField
from django.forms import *
from ast import literal_eval


class Contratform(ModelForm):
    mode_de_paiement = ChoiceField(choices=literal_eval(get_mode_de_paiement(1)))
    date_de_paiement = ChoiceField(choices=literal_eval(get_date_de_paiement(1)))

    class Meta:
        model = contrat
        fields = ['civilite', 'nom', 'prenom', 'date_de_naissance', 'regime', 'email', 'telephone',
                  'date_effet', 'date_de_paiement', 'mode_de_paiement']

        # fields = '__all__'

