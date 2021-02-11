from django.shortcuts import render

# Create your views here.

def config(request):
    context = None
    return render (request, 'config/config.html', context)
