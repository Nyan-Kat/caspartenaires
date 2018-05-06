# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-06 21:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tarification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrat',
            name='code_postal',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='date_effet',
            field=models.DateField(default=datetime.datetime(2018, 5, 6, 21, 29, 21, 528702, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='numero_securite_sociale',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='contrat',
            name='telephone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
