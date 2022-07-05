from tkinter import CASCADE
from django.db import models
# from .filesize import ContentTypeRestrictedFileField
from CrossShare.settings import BASE_DIR, MEDIA_ROOT
import uuid
import os
# Create your models here.
class uploadFile(models.Model):
    
    title = models.CharField(max_length=50)
    uuid = models.CharField(max_length=30 ,default = uuid.uuid4)
    file = models.FileField(upload_to=MEDIA_ROOT,null=True,blank=True,default="")
    # file = ContentTypeRestrictedFileField(content_types=['image/jpg', 'image/png', 'image/jpeg'],
    #     max_upload_size=5242880,
    #     null = True, blank=True, upload_to=MEDIA_ROOT, default="")
    created_at = models.CharField(max_length=30)

    def __str__(self):
            return self.title

# class Folder(models.Model):
#     uid = models.UUIDField(primary_key=True,default=uuid.uuid4)
#     created_at = models.DateField(auto_now=True)

# def upload_path(instance,filename):
#     return os.path.join(str(instance.folder.uid),filename)

# class Files(models.Model):
#     folder = models.ForeignKey(Folder,on_delete=models.CASCADE)
#     file = models.FileField(upload_to=upload_path)
#     created_at = models.DateField(auto_now = True)
