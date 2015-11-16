# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0011_noticia_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='tag',
            field=models.CharField(default=b'BLU', max_length=50),
            preserve_default=True,
        ),
    ]
