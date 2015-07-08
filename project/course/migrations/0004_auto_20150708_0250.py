# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20150703_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='instructor',
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ForeignKey(default=1, to='course.Instructor'),
            preserve_default=False,
        ),
    ]
