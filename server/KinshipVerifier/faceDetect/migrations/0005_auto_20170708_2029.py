# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 00:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faceDetect', '0004_auto_20170708_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='picturedata',
            name='data',
            field=models.CharField(default='0000000', max_length=1000),
        ),
        migrations.AddField(
            model_name='picturedata',
            name='file',
            field=models.ImageField(default='False.jpg', upload_to='geo_entity_pic'),
        ),
    ]