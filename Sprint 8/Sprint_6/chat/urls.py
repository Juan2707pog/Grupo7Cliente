from django.urls import path  
from .views import chat_details, chat_list


urlpatterns = [     
path('', chat_list),
path('<slug:value>/', chat_details),
]