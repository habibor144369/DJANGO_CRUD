# Generated by Django 3.2 on 2021-05-20 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_App', '0002_alter_album_num_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True),
        ),
    ]
