# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20150705_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='type',
            field=models.CharField(max_length=10, null=True, verbose_name='File type', blank=True),
            preserve_default=True,
        ),
    ]
