# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-29 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database1', '0021_auto_20180529_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golf_course',
            name='name',
            field=models.CharField(help_text=b'Golf Course Name', max_length=25),
        ),
    ]
