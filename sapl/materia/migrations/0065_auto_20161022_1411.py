# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-22 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0064_auto_20161022_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposicao',
            name='content_type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Tipo de Material Gerado'),
        ),
    ]
