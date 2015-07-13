# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import course.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_auto_20150712_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='bio',
            field=models.TextField(default=False),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='git',
            field=models.URLField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='pic',
            field=models.ImageField(default=False, upload_to=course.models.generate_imagename),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='twitter',
            field=models.URLField(default=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='website',
            field=models.URLField(default=False, max_length=100),
        ),
    ]
