from django.urls import path  
from .views import feed_details, feed_list


urlpatterns = [     
path('', feed_list),
path('<slug:value>/', feed_details),
]