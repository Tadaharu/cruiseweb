# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cruiseWeb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObtainedDataCA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationOne', models.CharField(max_length=100)),
                ('locationTwo', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('dataOrigin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cruiseWeb.ObtainedDataNER')),
            ],
        ),
    ]
