# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-21 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0010_auto_20170121_1535'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Utilisateur',
            new_name='Utilisateurs',
        ),
        migrations.AlterModelTable(
            name='utilisateurs',
            table='t_utilisateur',
        ),
    ]
