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
from . forms import UploadFileForm
from django.db import models
import os

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
        

class upload_model(APIView):

    def get(self, format=None):
        pass

# dont using swagger api 
def fileUploaderView(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                url = url = os.path.join('./home/model/models/',request.FILES['file'].name)
                ver = request.POST['version']
                upload(request.FILES['file'], ver)
                data = {
                    'version' : ver,
                    'url' : url
                }
                return HttpResponse(url + ver)
                # return HttpResponse("<h2>File uploaded successful!</h2>")
            else:
                return HttpResponse("<h2>File uploaded not successful!</h2>")
    
        form = UploadFileForm()
        return render(request, 'fileUploaderTemplate.html', {'form':form})
  
def upload(f,ver): 
    url = os.path.join('./home/model/models/',f.name)
    file = open(url, 'wb+') 
    for chunk in f.chunks():
        file.write(chunk)
    # add model to db
    dl_model = DLModel(modelUrl=url, modelVersion=ver)
    dl_model.save()