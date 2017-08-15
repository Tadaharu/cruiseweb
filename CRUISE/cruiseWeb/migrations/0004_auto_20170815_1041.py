# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruiseWeb', '0003_tweet_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='completed',
        ),
        migrations.AddField(
            model_name='tweet',
            name='completedCount',
            field=models.IntegerField(default=0),
        ),
    ]