from django.contrib import admin
from django.urls import path , include
from .views import hello


urlpatterns = [
    
    path('',view=hello,name='hello'),
    path('api/v1/' , include('user.api.v1.urls'))
]
