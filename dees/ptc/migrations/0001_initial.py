# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('appat', models.CharField(max_length=255)),
                ('apmat', models.CharField(max_length=255)),
                ('mail', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
                ('depto', models.CharField(max_length=255)),
                ('academia', models.CharField(max_length=255)),
            ],
        ),
    ]
