# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-04 14:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compilacao', '0063_tipotextoarticulado_publicacao_func'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='textoarticulado',
            options={'ordering': ['-data', '-numero'], 'permissions': (('view_restricted_textoarticulado', 'Pode ver qualquer Texto Articulado'),), 'verbose_name': 'Texto Articulado', 'verbose_name_plural': 'Textos Articulados'},
        ),
        migrations.AddField(
            model_name='textoarticulado',
            name='editable_only_by_owners',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Editável apenas pelos donos do Texto Articulado'),
        ),
        migrations.AddField(
            model_name='textoarticulado',
            name='editing_locked',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Texto Articulado em Edição'),
        ),
        migrations.AddField(
            model_name='textoarticulado',
            name='owners',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Donos do Texto Articulado'),
        ),
        migrations.AddField(
            model_name='textoarticulado',
            name='visibilidade',
            field=models.IntegerField(choices=[(99, 'Privado'), (79, 'Restrito'), (89, 'Em Edição'), (0, 'Público')], default=99, verbose_name='Visibilidade'),
        ),
        migrations.AlterField(
            model_name='tipotextoarticulado',
            name='publicacao_func',
            field=models.NullBooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Histórico de Publicação'),
        ),
    ]
