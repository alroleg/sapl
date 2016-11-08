# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-07 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compilacao', '0066_auto_20161107_1028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='textoarticulado',
            options={'ordering': ['-data', '-numero'], 'permissions': (('view_restricted_textoarticulado', 'Pode ver qualquer Texto Articulado'), ('lock_unlock_textoarticulado', 'Pode bloquear/desbloquear edição de Texto Articulado')), 'verbose_name': 'Texto Articulado', 'verbose_name_plural': 'Textos Articulados'},
        ),
    ]
