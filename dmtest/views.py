
from rest_framework.views import APIView
from rest_framework import status
from django.conf.urls import url
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import DatamodelSerializer

from .models import Datamodel

import requests

url = "http://my-json-server.typicode.com/rtavenar/fake_api/tasks"

reponse = requests.get(url)
print(reponse)
# Create your views here.
@api_view(['GET'])
def dmtestOverview(request):
    dmtest_urls = {
		'status':'True',
		}
    return JsonResponse({'dmtest_urls':dmtest_urls}) 

def profile_page(request, username=None):
    user = url.objects.get(username=username)
    message = request.GET.get('message')    

@api_view(['GET'])
def snippet_list(request):
            return JsonResponse(status="True")



@api_view(['GET'])
def namelist(request):
    names = Datamodel.objects.all()
    serializer = DatamodelSerializer(names, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def namedetail(request, pk):
    names = Datamodel.objects.get(id=pk)
    serializer = DatamodelSerializer(names, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def namecreate(request, pk):
    
    serializer = DatamodelSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def nameupdate(request, pk):
    
    names = Datamodel.objects.get(id=pk)
    serializer = DatamodelSerializer(instance=names, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)  

@api_view(['DELETE'])
def namedelete(request, pk):
	name = Datamodel.objects.get(id=pk)
	name.delete()

	return Response('Item succsesfully delete!') 



def special(request):
	

	return JsonResponse("Item succsesfully delete!", safe=False)     


def special2(request):
	

	return JsonResponse("Item succsesfully delete!", safe=False)    
    
      










     
