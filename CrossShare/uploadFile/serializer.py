from unittest.util import _MAX_LENGTH

from requests import request
from .models import uploadFile,Folder,Files
from rest_framework import serializers

class fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = uploadFile
        fields = ('id','title','uuid','file','created_at')



        

# class FileListSerializer(serializers.Serializer):
#     files = serializers.ListField(
#         child = serializers.FileField(max_length = 100000,allow_empty_file = False,use_url = False)
#     )
#     folder = serializers.CharField(required = False)

#     def create(self,validated_data):
#         folder = Folder.objects.create()
#         files = validated_data.pop('files')
#         files_objs = []
#         for file in files : 
#             files_obj = Files.objects.create(folder = folder,file = file)
#             files_objs.append(files_obj)

#         return files_obj