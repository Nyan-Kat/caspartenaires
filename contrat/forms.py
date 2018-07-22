from contrat.models import *
# from django.forms import ModelForm, DateField
from django.forms import *
from ast import literal_eval
from django.forms.widgets import *


# class ContratForm(ModelForm):
#     mode_de_paiement = ChoiceField(choices=literal_eval(get_mode_de_paiement(5)))
#     date_de_paiement = ChoiceField(choices=literal_eval(get_date_de_paiement(5)))
#
#     class Meta:
#         model = Contrat
#         fields = ['civilite', 'nom', 'prenom', 'date_de_naissance', 'regime', 'email', 'telephone',
#                   'date_effet', 'date_de_paiement', 'mode_de_paiement']
#
#         # fields = '__all__'


class ContratForm1(ModelForm):
    date_de_paiement = ChoiceField(choices=literal_eval(get_date_de_paiement(3)))

    class Meta:
        model = Contrat
        fields = ['civilite', 'nom', 'prenom', 'date_de_naissance', 'regime', 'email', 'telephone',
                  'date_effet', 'date_de_paiement', 'situation_familliale', 'adresse1', 'adresse2', 'code_postal',
                  'ville']
        # widgets = {
        #     'id': widgets.HiddenInput(),
        # }
        # fields = '__all__'


class ContratForm2(ModelForm):
    mode_de_paiement = ChoiceField(choices=literal_eval(get_mode_de_paiement(6)))

    class Meta:
        model = Contrat
        fields = ['id', 'mode_de_paiement']
        widgets = {
            'id': widgets.HiddenInput(),
        }
        # fields = '__all__'


# class ContratForm3(ModelForm):
#     mode_de_paiement = ChoiceField(choices=literal_eval(get_mode_de_paiement(6)))
#
#     class Meta:
#         model = Contrat
#         fields = ['id', 'mode_de_paiement']
#         # widgets = {
#         #     'id': widgets.HiddenInput(),
#         # }
#         # fields = '__all__'
