# Generated by Django 3.1.2 on 2020-10-29 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MobApp', '0003_stat_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='character_key',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]