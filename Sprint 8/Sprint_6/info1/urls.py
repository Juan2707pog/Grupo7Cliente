from django.urls import path  
from .views import info_details, info_list


urlpatterns = [     
path('', info_list),
path('<slug:value>/', info_details),
]