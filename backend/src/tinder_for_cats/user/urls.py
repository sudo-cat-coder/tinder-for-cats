from django.contrib import admin
from django.urls import path , include
from .views import hello
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    
    path('',view=hello,name='hello'),
    path('api/v1/' , include('tinder_for_cats.user.api.v1.urls'))

]


urlpatterns += [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]