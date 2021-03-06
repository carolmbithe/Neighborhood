# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-22 07:13
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='occupant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
