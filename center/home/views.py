from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseServerError, JsonResponse
from . model import hashModelH5
import json
from .models import DLModel
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
import coreapi
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

class test_swagger(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        return Response("OK")

class get_model_by_version(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, ver, format=None):
        model_obj = DLModel.objects.get(modelVersion=ver) # compare version 
        if model_obj :
            data = { # data's type is json 
                "version":model_obj.modelVersion,
                "url":model_obj.modelUrl
            }
            return Response(data)
        else:
            return Response("Fail to get model")


class add_model_manual(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, ver, url, format=None):
        dl_model = DLModel(modelUrl=url, modelVersion=ver)
        dl_model.save()
        return Response("Add successfully .") 
        




