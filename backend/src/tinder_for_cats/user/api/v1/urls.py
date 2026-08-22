from profile import Profile

from rest_framework import routers
from django.urls import include , path
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

# urlpatterns = [
#     #...
#     path("", UserViewSet.as_view({'get' : 'list' , 'post' : 'list'})),
#     path("?<int:id>", UserViewSet.as_view({'get' : 'id'})),
#]

# router = DefaultRouter() 
# router.register('',UserAPiView,basename='post')
# router.register('<int:id>' , UserAPiView, basename='user-detail')
# # router.register('',UserViewSet,basename='post')

urlpatterns = [
    path('', UserAPiView.as_view(), name='user-list'),
    path('<int:id>/', UserAPiView.as_view(), name='user-detail'),

    #sign in
    path('signup' , view=userSignUp.as_view()),

    #profile update
    path('profile/<int:pk>' , ProfileUpdate.as_view()),
    path('profile/<int:pk>/likes' , Add_likes),
    path('profile/' , AllProfile.as_view()),

]
