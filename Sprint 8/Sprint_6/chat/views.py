from django.shortcuts import render
from django.http import HttpResponse
from chat.models import chatnombres

# Create your views here.

def chat(request):
    context = None
    return render (request, 'chat/chat.html', context)

def chatuser(request):
    user_list = chatnombres.objects.order_by('first_name')
    user_dict = {'chat': user_list}
    return render(request, 'chat/chat.html', context=user_dict)