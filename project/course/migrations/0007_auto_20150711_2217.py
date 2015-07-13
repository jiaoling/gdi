# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import course.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20150711_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='content',
            field=models.FileField(default=False, upload_to=course.models.generate_filename),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='pic',
            field=models.ImageField(upload_to=course.models.generate_imagename),
        ),
    ]
