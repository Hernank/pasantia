# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0013_categoria_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='imagen_libro',
            field=models.ImageField(upload_to=b'images_books'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entrada',
            name='libro',
            field=models.FileField(upload_to=b'file_books'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticia',
            name='imagen_noticia',
            field=models.ImageField(upload_to=b'news', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='imagenperfil',
            field=models.ImageField(upload_to=b' imageperfil_users', blank=True),
            preserve_default=True,
        ),
    ]
