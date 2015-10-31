# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20151029_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='patente',
            field=models.CharField(unique=True, max_length=12),
        ),
    ]
