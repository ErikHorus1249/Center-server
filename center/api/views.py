from rest_framework import generics
from .models import Model_DL
from .serializers import ModelDlSerializer

class ModelDlList(generics.ListCreateAPIView):
    queryset = Model_DL.objects.all()
    serializer_class = ModelDlSerializer

class ModelDlDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Model_DL.objects.all()
    serializer_class = ModelDlSerializer