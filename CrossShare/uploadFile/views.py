from django.core.files import File
from CrossShare.settings import BASE_DIR, MEDIA_ROOT
from django.http import HttpResponse

from .models import uploadFile
from .serializer import fileSerializer
from rest_framework import generics
from rest_framework.decorators import api_view

# from rest_framework.decorators import parser_classes
from rest_framework.parsers import FormParser,MultiPartParser,FileUploadParser
# Create your views here.

class fileListCreateView(generics.ListCreateAPIView):
    # parser_classes = [FormParser,MultiPartParser]
    # queryset = uploadFile.objects.all()
    serializer_class= fileSerializer
    def get_queryset(self,**kwargs):
        if(self.request.method=='GET'):
            queryset = uploadFile.objects.all()
            uuid = self.kwargs.get('uuid',None)

            if uuid is not None:
                queryset = queryset.filter(uuid=uuid)
            return queryset

class fileRetreiveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):

    # lookup_field='uuid'
    # uuid = 'uuid'
    queryset = uploadFile.objects.all()
    serializer_class= fileSerializer
    