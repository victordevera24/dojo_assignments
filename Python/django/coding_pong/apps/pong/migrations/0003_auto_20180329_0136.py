# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-29 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pong', '0002_auto_20180328_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='loss',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='win',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]