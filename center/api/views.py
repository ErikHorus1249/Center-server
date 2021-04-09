from rest_framework import generics
from .models import Model_DL
from .serializers import ModelDlSerializer
from rest_framework.response import Response

from rest_framework.viewsets import ViewSet
from .serializers import UploadSerializer

class ModelDlList(generics.ListCreateAPIView):
    queryset = Model_DL.objects.all()
    serializer_class = ModelDlSerializer

class ModelDlDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Model_DL.objects.all()
    serializer_class = ModelDlSerializer

# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):
        return Response("GET API")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
    
