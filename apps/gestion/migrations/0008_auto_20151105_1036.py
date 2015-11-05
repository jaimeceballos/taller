# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_cliente_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='estado',
            field=models.IntegerField(),
        ),
    ]
