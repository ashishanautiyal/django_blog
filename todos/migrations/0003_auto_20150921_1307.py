# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20150918_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
