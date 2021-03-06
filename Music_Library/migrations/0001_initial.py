# Generated by Django 3.1 on 2020-10-29 03:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicLib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('song', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['mp3'], 'allow fileeteoion mp3')])),
                ('artist', models.CharField(max_length=25)),
            ],
        ),
    ]
