# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('manager', '0004_auto_20150926_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacebookStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(default=b'draft', max_length=255, choices=[(b'draft', b'Draft'), (b'approved', b'Approved')])),
                ('publish_timestamp', models.DateTimeField(null=True, blank=True)),
                ('message', models.TextField(max_length=255)),
                ('link', models.URLField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['publish_timestamp'],
                'verbose_name_plural': 'Facebook Statuses',
            },
            bases=(models.Model,),
        ),
    ]
