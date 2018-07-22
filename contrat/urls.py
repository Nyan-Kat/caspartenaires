#-*- coding: utf8 -*-
from django.conf.urls import url
from contrat.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^creer_contrat_step1/$', CreateContrat1.as_view(), name='creercontrat1'),
    url(r'^creer_contrat_step2/(?P<contrat_id>\d+)', CreateContrat2.as_view(), name='creercontrat2'),
    url(r'^tarification_rapide/$', home, name='home'),
    url(r'^devis_attente/$', home, name='home'),
    url(r'^contrats_refuses/$', home, name='home'),
    url(r'^historique/$', home, name='home'),

]

