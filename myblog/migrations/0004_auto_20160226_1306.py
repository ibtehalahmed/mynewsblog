# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20160226_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_publish_date',
            field=models.DateTimeField(),
        ),
    ]
