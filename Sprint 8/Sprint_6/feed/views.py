from django.shortcuts import render
from feed.models import User

# Create your views here.

def feed(request):
    context = None
    return render (request, 'feed/feed.html', context)

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'feed/feed.html', context=user_dict)
