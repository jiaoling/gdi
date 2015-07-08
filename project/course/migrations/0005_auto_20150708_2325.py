# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import any_urlfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20150708_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='meetup_page',
            field=any_urlfield.models.fields.AnyUrlField(max_length=300, verbose_name=b'URL'),
        ),
    ]
