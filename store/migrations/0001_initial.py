# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('country', models.CharField(max_length=100, verbose_name='Country')),
                ('city', models.CharField(max_length=100, verbose_name='City')),
                ('population', models.IntegerField(verbose_name='Population')),
            ],
        ),
    ]
