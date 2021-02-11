from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    context = None
    return render (request, 'register/register.html', context)
