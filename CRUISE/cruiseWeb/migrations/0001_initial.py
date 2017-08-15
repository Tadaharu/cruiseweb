# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 07:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObtainedDataNER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tLocation', models.CharField(max_length=300)),
                ('tState', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetText', models.CharField(max_length=264)),
                ('createdDate', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='obtaineddataner',
            name='tweet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cruiseWeb.Tweet'),
        ),
    ]