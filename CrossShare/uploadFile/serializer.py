from .models import uploadFile
from rest_framework import serializers

class fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = uploadFile
        fields = ('id','title','file','created_at')