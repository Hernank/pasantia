# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0008_auto_20151011_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
