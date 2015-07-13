# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import course.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20150711_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='pic',
            field=models.ImageField(upload_to=course.models.generate_filename),
        ),
    ]
