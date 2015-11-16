# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id_noticia', models.AutoField(serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=150)),
                ('imagen_noticia', models.ImageField(upload_to=b'uploads', blank=True)),
                ('contenido', models.CharField(max_length=50)),
                ('fecha_publicacion', models.DateField()),
                ('autor', models.ForeignKey(to='manager.Usuario')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='titulo',
            field=models.CharField(max_length=150),
        ),
    ]
