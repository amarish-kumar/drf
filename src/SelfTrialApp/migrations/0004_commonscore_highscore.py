# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SelfTrialApp', '0003_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hindi', models.PositiveIntegerField()),
                ('english', models.PositiveIntegerField()),
                ('mathematics', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HighScore',
            fields=[
                ('commonscore_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='SelfTrialApp.CommonScore')),
                ('social_science', models.PositiveIntegerField()),
                ('environment', models.PositiveIntegerField()),
                ('sanskrit', models.PositiveIntegerField()),
                ('fullname', models.ForeignKey(to='SelfTrialApp.Student')),
            ],
            bases=('SelfTrialApp.commonscore',),
        ),
    ]
