# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-20 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilacao', '0054_auto_20160916_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='dispositivo',
            name='dispositivo_de_revogacao',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Dispositivo de Revogação'),
        ),
    ]
