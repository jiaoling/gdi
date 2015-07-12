# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import course.models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20150712_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='git',
            field=models.URLField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='pic',
            field=models.ImageField(null=True, upload_to=course.models.generate_imagename),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='twitter',
            field=models.URLField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='website',
            field=models.URLField(max_length=100, null=True),
        ),
    ]
