# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-01 05:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmetadata', '0005_metadatasettings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadatasettings',
            name='site',
        ),
        migrations.DeleteModel(
            name='MetadataSettings',
        ),
    ]
