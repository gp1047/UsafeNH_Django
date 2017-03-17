# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 20:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collection', '0007_auto_20170317_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='user',
        ),
        migrations.AddField(
            model_name='college',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='College', to=settings.AUTH_USER_MODEL),
        ),
    ]
