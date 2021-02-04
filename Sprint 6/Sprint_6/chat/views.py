from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chat(request):
    context = None
    return render (request, 'chat/chat.html', context)
