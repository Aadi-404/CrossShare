from django.contrib import admin
from.models import Files, Folder, uploadFile
# Register your models here.

admin.site.register(uploadFile)
admin.site.register(Folder)
admin.site.register(Files)