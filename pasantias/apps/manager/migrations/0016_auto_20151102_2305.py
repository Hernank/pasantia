# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0015_entrada_librourl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='libro',
            field=models.FileField(null=True, upload_to=b'file_books', blank=True),
            preserve_default=True,
        ),
    ]
