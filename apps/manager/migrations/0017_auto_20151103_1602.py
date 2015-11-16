# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0016_auto_20151102_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='imagenperfil',
            field=models.ImageField(null=True, upload_to=b' imageperfil_users', blank=True),
            preserve_default=True,
        ),
    ]
