# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import course.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0015_auto_20150716_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='content',
            field=models.FileField(null=True, upload_to=course.models.generate_filename, blank=True),
        ),
    ]
