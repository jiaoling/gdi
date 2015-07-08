# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20150708_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='meetup_page',
            field=models.URLField(),
        ),
    ]
