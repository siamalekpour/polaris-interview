# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Continent',
                'verbose_name_plural': 'Continents',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('continent', models.ForeignKey(to='trips.Continent')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('latitude', models.CharField(max_length=20, verbose_name='LatLang')),
                ('longitude', models.CharField(max_length=20, verbose_name='LatLang')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date & Time')),
            ],
            options={
                'ordering': ['date'],
                'verbose_name': 'Destination',
                'verbose_name_plural': 'Destinations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DestinationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Unique Identifier')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Destination Type',
                'verbose_name_plural': 'Destination Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'')),
                ('type', models.CharField(max_length=10, verbose_name='File type')),
                ('destination', models.ForeignKey(to='trips.Destination')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MediaComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('media', models.ForeignKey(to='trips.Media')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('journal', models.TextField(null=True, verbose_name='Journal', blank=True)),
            ],
            options={
                'verbose_name': 'Traveler',
                'verbose_name_plural': 'Travelers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('country', models.ForeignKey(to='trips.Country')),
            ],
            options={
                'verbose_name': 'Trip',
                'verbose_name_plural': 'Trips',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TripType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Trip Type',
                'verbose_name_plural': 'Trip Types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='trip',
            name='type',
            field=models.ForeignKey(to='trips.TripType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='traveler',
            name='trip',
            field=models.ForeignKey(to='trips.Trip'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='traveler',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='destination',
            name='trip',
            field=models.ForeignKey(to='trips.Trip'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='destination',
            name='type',
            field=models.ForeignKey(to='trips.DestinationType'),
            preserve_default=True,
        ),
    ]
