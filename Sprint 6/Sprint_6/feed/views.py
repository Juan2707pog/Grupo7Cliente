from django.shortcuts import render

# Create your views here.

def feed(request):
    context = None
    return render (request, 'feed/feed.html', context)
