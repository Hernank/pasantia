# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_auto_20150918_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
