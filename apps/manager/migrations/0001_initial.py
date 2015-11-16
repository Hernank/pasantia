# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id_entrada', models.AutoField(serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('imagen_libro', models.ImageField(upload_to=b'uploads')),
                ('resumen', models.TextField()),
                ('fecha_publicacion', models.DateField()),
                ('libro', models.FileField(upload_to=b'')),
            ],
            options={
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Entradas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(blank=True, max_length=20, null=True, choices=[(b'male', b'Male'), (b'female', b'Female')])),
                ('city', models.CharField(max_length=250, null=True, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('locale', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('rol', models.CharField(default=b'User', max_length=50, null=True, blank=True)),
                ('imagenperfil', models.ImageField(upload_to=b' images', blank=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entrada',
            name='autor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entrada',
            name='categoria',
            field=models.ForeignKey(to='manager.Categoria'),
            preserve_default=True,
        ),
    ]
