from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    context = None
    return render (request, 'login/login.html', context)
