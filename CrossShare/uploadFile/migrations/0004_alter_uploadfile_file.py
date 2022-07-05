# Generated by Django 4.0.1 on 2022-06-12 06:17

from django.db import migrations
import pathlib
import uploadFile.filesize


class Migration(migrations.Migration):

    dependencies = [
        ('uploadFile', '0003_alter_uploadfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=uploadFile.filesize.ContentTypeRestrictedFileField(blank=True, default='', null=True, upload_to=pathlib.PureWindowsPath('C:/Code/web/django/shareFile/CrossShare/media')),
        ),
    ]