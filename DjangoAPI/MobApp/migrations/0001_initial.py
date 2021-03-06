# Generated by Django 3.1.2 on 2020-10-25 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('character_id', models.AutoField(primary_key=True, serialize=False)),
                ('character_name', models.CharField(max_length=20)),
                ('character_description', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(verbose_name='Date Created')),
                ('character_photofilename', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('race_id', models.AutoField(primary_key=True, serialize=False)),
                ('race_name', models.CharField(max_length=20)),
                ('race_description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strength', models.IntegerField(default=0)),
                ('perception', models.IntegerField(default=0)),
                ('charisma', models.IntegerField(default=0)),
                ('speed', models.IntegerField(default=0)),
                ('intellect', models.IntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MobApp.character')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MobApp.race'),
        ),
    ]
