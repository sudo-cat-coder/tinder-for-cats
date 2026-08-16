from rest_framework import routers
from django.urls import include , path
from .views import UserViewSet


urlpatterns = [
    #...
    path("", UserViewSet.as_view({'get' : 'list'})),
]