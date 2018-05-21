#-*- coding: utf8 -*-
from django.conf.urls import url
from contrat.views import *

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^creer_contrat/$', CreateContrat.as_view(), name='createcontrat'),
    url(r'^tarification_rapide/$', home, name='home'),
    url(r'^devis_attente/$', home, name='home'),
    url(r'^contrats_refuses/$', home, name='home'),
    url(r'^historique/$', home, name='home'),

]

