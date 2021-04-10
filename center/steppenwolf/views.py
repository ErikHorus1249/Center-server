from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
# from rest_framework.response import Response
from django.http import HttpResponse
# from rest_framework import status
from .serializers import FileSerializer

from rest_framework import permissions
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

class FileView(APIView):
  # permission_classes = [permissions.IsAuthenticated]
  parser_classes = (MultiPartParser, FormParser)

  @swagger_auto_schema(operation_description='Upload file...',)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    fl = request.POST.get("file")
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data)
    else:
      return Response(file_serializer.errors)
  
  # def post(self, request, *args, **kwargs):
  #       """
  #           Create a MyModel
  #           ---
  #           parameters:
  #               - name: file
  #                 description: file
  #                 required: True
  #                 type: file
  #           responseMessages:
  #               - code: 201
  #                 message: Created
  #       """
  #       return self(FileView, self).post(self, *args, **kwargs)

# using for path testing
class TestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return HttpResponse("successful")