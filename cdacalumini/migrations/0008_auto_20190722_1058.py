# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-22 05:28
from __future__ import unicode_literals

import cdacalumini.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cdacalumini', '0007_auto_20190722_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Deadline',
            field=models.DateField(validators=[cdacalumini.models.no_future]),
        ),
    ]
