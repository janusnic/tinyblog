# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('status', models.CharField(default='0', choices=[('0', 'Draft'), ('1', 'Published'), ('2', 'Not Published')], max_length=1)),
                ('title', models.CharField(max_length=32)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('content', models.TextField()),
                ('featured_image', models.ImageField(null=True, upload_to=blog.models.get_blog_file_name, blank=True, max_length=1024)),
            ],
        ),
    ]
