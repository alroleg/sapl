# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-29 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0014_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='legislacaocitada',
            options={'verbose_name': 'Legislação', 'verbose_name_plural': 'Legislações'},
        ),
    ]