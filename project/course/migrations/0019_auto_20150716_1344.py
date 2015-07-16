# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0018_auto_20150716_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='link_content',
            field=models.URLField(max_length=500, null=True, blank=True),
        ),
    ]
