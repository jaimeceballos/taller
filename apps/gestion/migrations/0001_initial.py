# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('telefono_caracteristica', models.CharField(max_length=5, null=True)),
                ('telefono_numero', models.CharField(max_length=10, null=True)),
                ('direccion', models.CharField(max_length=100, null=True)),
                ('otro_contacto', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClienteVehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('fecha_hasta', models.DateField()),
                ('cliente', models.ForeignKey(related_name='tiene', to='gestion.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_ingreso', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('km_ingreso', models.IntegerField()),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_vehiculo', models.CharField(max_length=20, choices=[(b'auto', b'AUTO'), (b'camioneta', b'CAMIONETA'), (b'camion', b'CAMION'), (b'moto', b'MOTO')])),
                ('modelo_marca', models.CharField(max_length=100)),
                ('patente', models.CharField(max_length=12)),
                ('observaciones', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='trabajo',
            name='vehiculo',
            field=models.ForeignKey(related_name='trabajos_realizados', to='gestion.Vehiculo'),
        ),
        migrations.AddField(
            model_name='clientevehiculo',
            name='vehiculo',
            field=models.ForeignKey(related_name='pertenece_a', to='gestion.Vehiculo'),
        ),
    ]
