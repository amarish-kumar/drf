# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SelfTrialApp', '0011_auto_20170513_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonscore',
            name='fullname',
            field=models.ForeignKey(default=b'', to='SelfTrialApp.Student'),
        ),
    ]
