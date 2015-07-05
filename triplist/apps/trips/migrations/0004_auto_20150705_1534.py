# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20150701_1532'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AlterField(
            model_name='destination',
            name='latitude',
            field=models.CharField(max_length=20, verbose_name='Lattitude'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='destination',
            name='longitude',
            field=models.CharField(max_length=20, verbose_name='Longitude'),
            preserve_default=True,
        ),
    ]
