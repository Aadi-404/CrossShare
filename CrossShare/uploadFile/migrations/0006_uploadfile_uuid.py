# Generated by Django 4.0.1 on 2022-06-13 17:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('uploadFile', '0005_alter_uploadfile_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=30),
        ),
    ]
