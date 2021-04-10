from rest_framework import serializers
from .models import Model_DL
from rest_framework.serializers import Serializer, FileField


class ModelDlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model_DL
        fields = ('version_model', 'url_model')

# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']