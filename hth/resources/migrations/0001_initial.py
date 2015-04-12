# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=15)),
                ('fa_class', models.CharField(max_length=30)),
                ('background_image', models.FileField(upload_to=b'')),
                ('abstract', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('entry_type', models.CharField(max_length=1, choices=[(b'T', b'Tile'), (b'D', b'Detail')])),
            ],
        ),
        migrations.CreateModel(
            name='EntrySet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EntrySetRelationship',
            fields=[
                ('parent', models.OneToOneField(primary_key=True, serialize=False, to='resources.EntrySet')),
                ('sub_set', models.ForeignKey(related_name='+', to='resources.EntrySet')),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='entry_set',
            field=models.ForeignKey(to='resources.EntrySet'),
        ),
    ]
