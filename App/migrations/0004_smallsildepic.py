# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20181106_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmallSildePic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_src', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=1000)),
                ('discount_price', models.CharField(max_length=100)),
                ('orig_price', models.CharField(max_length=100)),
            ],
        ),
    ]