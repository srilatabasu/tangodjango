# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-24 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlackAskUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.TextField(default='')),
                ('team_id', models.TextField(default='')),
                ('team_domain', models.TextField(default='')),
                ('enterprise_id', models.TextField(default='')),
                ('enterprise_name', models.TextField(default='')),
                ('channel_id', models.TextField(default='')),
                ('channel_name', models.TextField(default='')),
                ('user_id', models.TextField(default='')),
                ('user_name', models.TextField(default='')),
                ('command', models.TextField(default='')),
                ('text', models.TextField(default='')),
                ('response_url', models.TextField(default='')),
                ('trigger_id', models.TextField(default='')),
            ],
        ),
    ]