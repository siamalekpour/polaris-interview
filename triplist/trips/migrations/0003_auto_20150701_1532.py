# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destinationtype',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
            preserve_default=True,
        ),
    ]
