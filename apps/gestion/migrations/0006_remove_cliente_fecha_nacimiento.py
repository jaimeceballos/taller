# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_cliente_fecha_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='fecha_nacimiento',
        ),
    ]
