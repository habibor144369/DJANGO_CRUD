# Generated by Django 3.2 on 2021-05-20 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_App', '0003_album_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='slug',
        ),
        migrations.AddField(
            model_name='musician',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True),
        ),
    ]