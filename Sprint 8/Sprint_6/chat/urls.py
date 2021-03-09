from django.urls import path  
from . import views


urlpatterns = [     
path('', views.chat_list),
path('<slug:value>/', views.chat_details),
]