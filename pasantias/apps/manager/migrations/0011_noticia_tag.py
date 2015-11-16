# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_auto_20151011_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='tag',
            field=models.CharField(default=b'BLU', max_length=50),
            preserve_default=True,
        ),
    ]
