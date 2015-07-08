# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c_name', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=20)),
                ('start_date', models.DateTimeField(null=True, blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('meetup_page', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prerequisite', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_name', models.CharField(max_length=80)),
                ('l_name', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('twitter', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('git', models.CharField(max_length=100)),
                ('bio', models.TextField()),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=20)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('course_id', models.ForeignKey(to='course.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='instructor',
            field=models.ManyToManyField(to='course.Instructor'),
        ),
        migrations.AddField(
            model_name='course',
            name='topic',
            field=models.ForeignKey(to='course.Topic'),
        ),
    ]
