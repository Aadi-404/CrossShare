# Generated by Django 4.0.1 on 2022-05-26 10:35

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='uploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to=pathlib.PureWindowsPath('C:/Code/web/django/shareFile/CrossShare/media'))),
                ('created_at', models.CharField(max_length=30)),
            ],
        ),
    ]