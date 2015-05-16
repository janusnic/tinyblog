# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150516_0618'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(max_length=1, choices=[('0', 'Draft'), ('1', 'Published'), ('2', 'Not Published')], default='0'),
        ),
    ]
