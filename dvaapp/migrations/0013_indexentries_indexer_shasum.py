# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 06:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0012_auto_20170829_0528'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexentries',
            name='indexer_shasum',
            field=models.CharField(default='cafecafecafecafecafecafecafecafecafecafe', max_length=40),
            preserve_default=False,
        ),
    ]