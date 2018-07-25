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


class ContratForm2(ModelForm):
    type_contrat = ModelChoiceField(queryset=TypeContrat.objects.order_by('nom'))
    produit = ModelChoiceField(queryset=Produit.objects.order_by('nom'))
    categorie_produit = ModelChoiceField(queryset=CategorieProduit.objects.order_by('nom'))

    class Meta:
        model = Contrat
        fields = ['id', 'type_contrat', 'produit', 'categorie_produit']
        widgets = {
            'id': widgets.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ContratForm2, self).__init__(*args, **kwargs)
        self.fields['produit'].queryset = Produit.objects.none()
        self.fields['categorie_produit'].queryset = CategorieProduit.objects.none()

        if 'type_contrat' in self.data:
            try:
                type_contrat_id = int(self.data.get('type_contrat'))
                self.fields['produit'].queryset = Produit.objects.filter(type_contrat_id=type_contrat_id).order_by('nom')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['produit'].queryset = self.instance.type_contrat.produit_set.order_by('nom')

        if 'produit' in self.data:
            try:
                produit_id = int(self.data.get('produit'))
                self.fields['categorie_produit'].queryset = CategorieProduit.objects.filter(produit_id=produit_id).order_by('nom')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['categorie_produit'].queryset = self.instance.produit.categorie_produit_set.order_by('nom')


class ContratForm4(ModelForm):
    mode_de_paiement = ChoiceField(choices=literal_eval(get_mode_de_paiement(6)))

    class Meta:
        model = Contrat
        fields = ['id', 'mode_de_paiement']
        widgets = {
            'id': widgets.HiddenInput(),
        }
