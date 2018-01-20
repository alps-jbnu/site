# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-20 20:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import judge.utils.generator


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0068_auto_20171229_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='student_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='student id'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='access_code',
            field=models.CharField(blank=True, default=judge.utils.generator.make_random_fruit, help_text='An optional code to prompt contestants before they are allowed to join the contest. Leave it blank to disable.', max_length=255, verbose_name='access code'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='key',
            field=models.CharField(default=judge.utils.generator.make_key, max_length=20, unique=True, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z0-9]+$', 'Contest id must be ^[a-z0-9]+$')], verbose_name='contest id'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='key',
            field=models.CharField(default=b'2018QC', help_text='Organization name shows in URL', max_length=6, unique=True, validators=[django.core.validators.RegexValidator(b'^[A-Za-z0-9]+$', b'Identifier must contain letters and numbers only')], verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='code',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(b'^[a-zA-Z0-9\\-]+$', 'Problem code must be ^[a-z0-9]+$')], verbose_name='problem code'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='memory_limit',
            field=models.IntegerField(default=131072, help_text='The memory limit for this problem, in kilobytes (e.g. 64mb = 65536 kilobytes).', verbose_name='memory limit'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='time_limit',
            field=models.FloatField(default=1.0, help_text='The time limit for this problem, in seconds. Fractional seconds (e.g. 1.5) are supported.', verbose_name='time limit'),
        ),
    ]
