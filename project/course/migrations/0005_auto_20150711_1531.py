# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20150708_0250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='course_id',
            new_name='course',
        ),
    ]
