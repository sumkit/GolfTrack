# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database1', '0009_auto_20171130_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, choices=[('g', 'golfer'), ('c', 'coach')], default='g', max_length=2)),
                ('team', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='database1.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='team',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
