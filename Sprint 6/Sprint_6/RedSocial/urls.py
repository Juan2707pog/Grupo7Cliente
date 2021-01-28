from django.urls import path  
from . import views  


urlpatterns = [     
path('login', views.login), 
path('register', views.register),
path('config', views.config),
path('post', views.post),
path('chat', views.chat),
path('info', views.info),
path('feed', views.feed),
path('header', views.header),
]