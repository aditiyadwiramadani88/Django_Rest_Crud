# Generated by Django 3.0.7 on 2020-08-17 09:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music_Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.FileField(max_length=200, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3'])])),
                ('album', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'music_library',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_playlist', models.CharField(max_length=200)),
                ('song', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('album', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'playlist',
            },
        ),
        migrations.CreateModel(
            name='Title_Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_playlist', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'title_playlist',
            },
        ),
    ]
