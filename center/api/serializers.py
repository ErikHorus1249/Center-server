from rest_framework import serializers
from .models import Model_DL


class ModelDlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model_DL
        fields = ('version_model', 'url_model')