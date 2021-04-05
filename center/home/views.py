from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseServerError, JsonResponse
from . model import hashModelH5
import json
# Create your views here.
def index(request):
    # bam model moi
    server_hashcode = hashModelH5.hashModel()
    data = {}
    if request.method == 'GET':

        response = HttpResponse()
        ana_hashcode = request.GET['q']
        
        # so khop voi model vua duoc gui den 
        response.writelines("server:"+server_hashcode)
        if hashModelH5.compareModel(server_hashcode,ana_hashcode):
            data = {
                'link':'https://raw.githubusercontent.com/ErikHorus1249/Web_Tutorials/master/DjangoTurtorial/turtorial1/home/model/hashModelH5.py'
                # add version + save db : 
                # su dung version so sanh
            }
        else:
            data = {
                'link':'invalid'
            }
        return JsonResponse(data)


def save_data(request):
    response = HttpResponse()
    if request.method == 'POST':
        json_data = json.loads(request.body) # request.raw_post_data w/ Django < 1.4
        try:
            data = json_data['data']
            response.write(data)
        except KeyError:
            HttpResponseServerError("Malformed data!")
        
    return response