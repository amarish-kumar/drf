# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SelfTrialApp', '0009_auto_20170513_0715'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HighScore',
            new_name='HighSchoolScore',
        ),
    ]
