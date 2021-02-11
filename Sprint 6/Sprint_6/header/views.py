from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def header(request):
    context = None
    return render (request, 'header/header.html', context)
