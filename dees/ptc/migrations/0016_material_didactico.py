# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-05 21:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptc', '0015_auto_20171225_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material_Didactico',
            fields=[
                ('id_mad', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_mad', models.CharField(max_length=255)),
                ('titulo_mad', models.CharField(max_length=255)),
                ('evidencia_mad', models.CharField(max_length=500)),
                ('year_mad', models.IntegerField()),
                ('profesor_mad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptc.Profesor')),
            ],
        ),
    ]
