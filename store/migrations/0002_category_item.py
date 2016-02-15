# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=100)),
                ('value_int', models.PositiveIntegerField(verbose_name='Number')),
                ('value_float', models.FloatField(verbose_name='Cost')),
                ('categories', models.ManyToManyField(to='store.Category')),
            ],
        ),
    ]
