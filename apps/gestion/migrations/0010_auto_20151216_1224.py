# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0009_auto_20151105_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefono_numero',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
