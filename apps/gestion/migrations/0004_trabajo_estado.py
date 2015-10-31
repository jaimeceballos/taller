# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0003_auto_20151030_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='estado',
            field=models.IntegerField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
