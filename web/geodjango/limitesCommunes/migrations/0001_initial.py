# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 14:23
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LimitesCommunes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_geofla', models.CharField(max_length=24)),
                ('code_com', models.CharField(max_length=3)),
                ('insee_com', models.CharField(max_length=5)),
                ('nom_com', models.CharField(max_length=50)),
                ('statut', models.CharField(max_length=25)),
                ('x_chf_lieu', models.IntegerField()),
                ('y_chf_lieu', models.IntegerField()),
                ('x_centroid', models.IntegerField()),
                ('y_centroid', models.IntegerField()),
                ('z_moyen', models.IntegerField()),
                ('superficie', models.FloatField()),
                ('population', models.IntegerField()),
                ('code_arr', models.CharField(max_length=1)),
                ('code_dept', models.CharField(max_length=2)),
                ('nom_dept', models.CharField(max_length=30)),
                ('code_reg', models.CharField(max_length=2)),
                ('nom_reg', models.CharField(max_length=35)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=2154)),
            ],
        ),
        migrations.CreateModel(
            name='Prefectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gml_id', models.CharField(max_length=100)),
                ('gid', models.IntegerField()),
                ('insee_commune', models.CharField(max_length=100)),
                ('nom_commune', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
    ]
