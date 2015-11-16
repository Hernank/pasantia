# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20150924_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='libro',
            field=models.FileField(upload_to=b'uploads'),
            preserve_default=True,
        ),
    ]
