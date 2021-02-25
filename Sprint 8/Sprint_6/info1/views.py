from django.db import reset_queries
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Infoinsta
from .serializers import info1Serializer

# Create your views here.

@csrf_exempt
def info_list(request):

    if request.method == 'GET':
        users = Infoinsta.objects.all()
        serializer = info1Serializer(users, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = info1Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=204)

@csrf_exempt
def info_details(request, value):

    try:
        user = Infoinsta.objects.get(nick_name=value)
    except Infoinsta.DoesNotExist:
        return HttpResponse(status=404)

    #Consultar
    if request.method == 'GET':
        serializer = info1Serializer(user)
        return JsonResponse(serializer.data, safe=False, status=200)

    #Modificar
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = info1Serializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)

    #Eliminar
    elif request.method == 'DELETE':
        try:
            user.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)
