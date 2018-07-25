#-*- coding: utf8 -*-
from django.conf.urls import url
from contrat.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^creer_contrat_step1/$', CreateContrat1.as_view(), name='creercontrat1'),
    url(r'^creer_contrat_step2/(?P<contrat_id>\d+)', CreateContrat2.as_view(), name='creercontrat2'),
    url(r'^ajax/load_produit/$', load_produit, name='ajax_load_produit'),
    url(r'^ajax/load_categorie_produit/$', load_categorie_produit, name='ajax_load_categorie_produit'),
    url(r'^creer_contrat_step4/(?P<contrat_id>\d+)', CreateContrat4.as_view(), name='creercontrat4'),
    url(r'^tarification_rapide/$', home, name='home'),
    url(r'^devis_attente/$', home, name='home'),
    url(r'^contrats_refuses/$', home, name='home'),
    url(r'^historique/$', home, name='home'),

]

