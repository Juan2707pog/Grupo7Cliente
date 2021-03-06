from django.shortcuts import render
from feed.models import User
from django.db import reset_queries
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import FeedSerializer

# Create your views here.

@csrf_exempt
def feed_list(request):

    if request.method == 'GET':
        feed_users = User.objects.all()
        serializer = FeedSerializer(feed_users, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = FeedSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=204)

@csrf_exempt
def feed_details(request, value):

    try:
        feed_user = User.objects.get(first_name=value)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    #Consultar
    if request.method == 'GET':
        serializer = FeedSerializer(feed_user)
        return JsonResponse(serializer.data, safe=False, status=200)

    #Modificar
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = FeedSerializer(feed_user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=204)

    #Eliminar
    elif request.method == 'DELETE':
        try:
            feed_user.delete()
            return HttpResponse(status=200)
        except:
            return HttpResponse(status=409)


#def feed(request):
    #context = None
    #return render (request, 'feed/feed.html', context)

#def users(request):
    #user_list = User.objects.order_by('first_name')
    #user_dict = {'users': user_list}
    #return render(request, 'feed/feed.html', context=user_dict)
