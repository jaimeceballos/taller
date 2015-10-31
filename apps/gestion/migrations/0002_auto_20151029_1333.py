# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='telefono_caracteristica',
        ),
        migrations.AddField(
            model_name='trabajo',
            name='precio',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='clientevehiculo',
            name='fecha_hasta',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='descripcion',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='fecha_entrega',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='fecha_ingreso',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='km_ingreso',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='tipo_vehiculo',
            field=models.CharField(max_length=20),
        ),
    ]
