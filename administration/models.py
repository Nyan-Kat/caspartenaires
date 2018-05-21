# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nom = models.CharField(max_length=100, default='')
    prenom = models.CharField(max_length=100, default='')
    telephone = models.CharField(max_length=10, default='')
    email = models.EmailField(default='')
