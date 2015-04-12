# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('abstract', models.CharField(max_length=100)),
                ('fa_class', models.CharField(max_length=20)),
                ('background_image', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryAbstractLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=2)),
                ('abstract', models.CharField(max_length=100)),
                ('category', models.ForeignKey(to='resources.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=15)),
                ('abstract', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address', models.TextField()),
                ('opening', models.TextField()),
                ('category', models.ForeignKey(to='resources.Category')),
            ],
        ),
        migrations.CreateModel(
            name='EntryAbstractLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=2)),
                ('abstract', models.CharField(max_length=100)),
                ('entry', models.ForeignKey(to='resources.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='EntryDescriptionLanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language', models.CharField(max_length=2)),
                ('description', models.TextField()),
                ('entry', models.ForeignKey(to='resources.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='EntryPhone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=12)),
                ('available', models.BooleanField()),
                ('entry', models.ForeignKey(to='resources.Entry')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='entrydescriptionlanguage',
            unique_together=set([('entry', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='entryabstractlanguage',
            unique_together=set([('entry', 'language')]),
        ),
        migrations.AlterUniqueTogether(
            name='categoryabstractlanguage',
            unique_together=set([('category', 'language')]),
        ),
    ]
