# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class LimitesCommunes(models.Model):
    id_geofla = models.CharField(max_length=24)
    code_com = models.CharField(max_length=3)
    insee_com = models.CharField(max_length=5)
    nom_com = models.CharField(max_length=50)
    statut = models.CharField(max_length=25)
    x_chf_lieu = models.IntegerField()
    y_chf_lieu = models.IntegerField()
    x_centroid = models.IntegerField()
    y_centroid = models.IntegerField()
    z_moyen = models.IntegerField()
    superficie = models.FloatField()
    population = models.IntegerField()
    code_arr = models.CharField(max_length=1)
    code_dept = models.CharField(max_length=2)
    nom_dept = models.CharField(max_length=30)
    code_reg = models.CharField(max_length=2)
    nom_reg = models.CharField(max_length=35)
    geom = models.MultiPolygonField(srid=2154)

class Prefectures(models.Model):
    gml_id = models.CharField(max_length=100)
    gid = models.IntegerField()
    insee_commune = models.CharField(max_length=100)
    nom_commune = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    geom = models.MultiPointField(srid=2154 )

