# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-26 21:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobinformation', '0005_auto_20160425_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='topic',
            new_name='topic_name',
        ),
    ]
