from rest_framework import routers
from django.urls import include , path
from .views import *
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     #...
#     path("", UserViewSet.as_view({'get' : 'list' , 'post' : 'list'})),
#     path("?<int:id>", UserViewSet.as_view({'get' : 'id'})),
#]

router = DefaultRouter() 
router.register('',UserViewSet,basename='post')
# router.register('',UserViewSet,basename='post')

urlpatterns = router.urls
