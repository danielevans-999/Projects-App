# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-11-24 21:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0004_auto_20191124_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(default='media/images/smoke.jpeg', upload_to='images/'),
        ),
    ]
