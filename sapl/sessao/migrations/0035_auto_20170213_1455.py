# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-13 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessao', '0034_votonominal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votonominal',
            name='expediente',
        ),
        migrations.RemoveField(
            model_name='votonominal',
            name='ordem',
        ),
    ]
