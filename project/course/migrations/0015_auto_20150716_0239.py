# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_auto_20150716_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='type',
            field=models.CharField(default=b'link', max_length=4, choices=[(b'link', b'add a link'), (b'file', b'add a file')]),
        ),
    ]
