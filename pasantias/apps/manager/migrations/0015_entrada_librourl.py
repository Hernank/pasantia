# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0014_auto_20151031_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='librourl',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
