# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 05:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0003_thing_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='College',
        ),
    ]
