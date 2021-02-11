from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def info1(request):
    context = None
    return render (request, 'info/info.html', context)
