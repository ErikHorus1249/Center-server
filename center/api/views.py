from rest_framework import generics
from .models import Model_DL
from .serializers import ModelDlSerializer
from rest_framework.response import Response

from rest_framework.viewsets import ViewSet
from rest_framework import viewsets
from .serializers import UploadSerializer

from rest_framework.views import APIView
from rest_framework import permissions

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
        return Response("GET API OK")

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "POST API and you have uploaded a {} file".format(content_type)
        return Response(response)
    
# class Model_DLViewSet(viewsets.ModelViewSet):
#     serializer_class = ModelDlSerializer
#     queryset = Model_DL.objects.all()
#     permission_classes = [permissions.IsAuthenticated]

#     ordering_fields = ('version_model', 'url_model')
#     ordering= ('version_model')
#     searcch_fields = ('version_model', 'url_model')
    