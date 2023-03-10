from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Register
from .serializers import RegisterSerializer

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def users_list(request):
    if request.method=='GET':
        users_lists=Register.objects.all()
        serializer=RegisterSerializer(users_lists,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method=="POST":
        data=JSONParser().parse(request)
        serializer=RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.error,status=400)