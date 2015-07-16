# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import course.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_auto_20150716_0132'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='link_content',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='content',
            field=models.FileField(null=True, upload_to=course.models.generate_filename),
        ),
    ]
