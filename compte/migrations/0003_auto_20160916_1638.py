# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-16 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compte', '0002_auto_20160916_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateurs',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='utilisateurs',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='utilisateurs',
            name='apropos',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateurs',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='utilisateurs',
            name='nbr_annonce',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='utilisateurs',
            name='nbr_cmd',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='utilisateurs',
            name='nbr_livraison',
            field=models.IntegerField(max_length=10),
        ),
        migrations.AlterField(
            model_name='utilisateurs',
            name='telephone',
            field=models.BigIntegerField(max_length=10),
        ),
    ]
