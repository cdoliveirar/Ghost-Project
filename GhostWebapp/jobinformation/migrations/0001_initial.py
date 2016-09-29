# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 16:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InformationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TextInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info_text', models.CharField(max_length=1000)),
                ('pup_date', models.DateTimeField(verbose_name='date published')),
                ('infotype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobinformation.InformationType')),
            ],
        ),
    ]
