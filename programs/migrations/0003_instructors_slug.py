# Generated by Django 2.2 on 2020-11-11 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0002_auto_20201109_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructors',
            name='slug',
            field=models.SlugField(default='slug'),
        ),
    ]
