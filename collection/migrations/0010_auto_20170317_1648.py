# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0009_auto_20170317_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='colleges',
            field=models.ManyToManyField(to='collection.College'),
        ),
    ]
