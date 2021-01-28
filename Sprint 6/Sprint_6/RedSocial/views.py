from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#def index(request):
 #   return HttpResponse("Hola puto reina.")

def login(request):
    context = None
    return render (request, 'RedSocial/login.html', context)

def register(request):
    context = None
    return render (request, 'RedSocial/register.html', context)

def header(request):
    context = None
    return render (request, 'RedSocial/header.html', context)

def config(request):
    context = None
    return render (request, 'RedSocial/config.html', context)

def post(request):
    context = None
    return render (request, 'RedSocial/post.html', context)

def chat(request):
    context = None
    return render (request, 'RedSocial/chat.html', context)

def info(request):
    context = None
    return render (request, 'RedSocial/info.html', context)

def feed(request):
    context = None
    return render (request, 'RedSocial/feed.html', context)

