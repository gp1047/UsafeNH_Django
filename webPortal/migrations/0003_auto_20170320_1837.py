# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 22:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webPortal', '0002_auto_20170320_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='college',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='user',
        ),
        migrations.AddField(
            model_name='hospital',
            name='collegeName',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='webPortal.College'),
        ),
    ]
