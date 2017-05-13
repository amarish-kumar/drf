# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SelfTrialApp', '0010_auto_20170513_0726'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrimarySchoolScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mathematics', models.PositiveIntegerField()),
                ('hindi', models.PositiveIntegerField()),
                ('english', models.PositiveIntegerField()),
                ('science', models.PositiveIntegerField()),
                ('environment', models.PositiveIntegerField()),
                ('fullname', models.ForeignKey(to='SelfTrialApp.Student')),
            ],
        ),
        migrations.RemoveField(
            model_name='primaryscore',
            name='fullname',
        ),
        migrations.DeleteModel(
            name='PrimaryScore',
        ),
    ]
