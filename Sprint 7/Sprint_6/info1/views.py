from info1.models import Infoinsta
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def info1(request):
    context = None
    return render (request, 'info/info.html', context)


def infouser(request):
    user_list = Infoinsta.objects.order_by('arroba')
    user_dict = {'infoinstagram': user_list}
    return render(request, 'info/info.html', context=user_dict)
