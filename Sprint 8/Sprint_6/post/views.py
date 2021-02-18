from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post(request):
    context = None
    return render (request, 'post/post.html', context)
