# Generated by Django 3.0.7 on 2020-08-17 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music_Library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='song',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='title_playlist',
            name='title_playlist',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]