from django.db import reset_queries
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import chatnombres
from .serializers import ChatSerializer

# Create your views here.

@csrf_exempt
def chat_list(request):

    if request.method == 'GET':
        users = chatnombres.objects.all()
        serializer = ChatSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=204)

@csrf_exempt
def chat_details(request, value):

    try:
        user = chatnombres.objects.get(first_name=value)
    except chatnombres.DoesNotExist:
        return HttpResponse(status=404)

    #Consultar
    if request.method == 'GET':
        serializer = ChatSerializer(user)
        return JsonResponse(serializer.data, safe=False, status=200)

    #Modificar
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ChatSerializer(user, data=data)
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

#def chat(request):
 #   context = None
  #  return render (request, 'chat/chat.html', context)


#def chatuser(request):
 #   user_list = chatnombres.objects.order_by('first_name')
  #  user_dict = {'chat': user_list}
   # return render(request, 'chat/chat.html', context=user_dict)