import re

from django.http import HttpResponse
from rest_framework.status import *
from rest_framework.authentication import SessionAuthentication
from ...models import User
from rest_framework import permissions, viewsets
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView, Response

from tinder_for_cats.user.api.v1 import serializer



# class UserViewSet(viewsets.ModelViewSet):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [permissions.IsAuthenticated]
    
class UserAPiView(APIView):

    # authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]

    def get(self,request,id=None):
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            print(self.kwargs)
            return Response(serializer.data)
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        # print(request.parsers[1])
        return Response(serializer.data)


# class UserApiView(APIView):

#     def post(self,request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.password1 == serializer.password2 and serializer.is_valid():
#             serializer.save()
#             return Response(HTTP_201_CREATED)



class userSignUp(APIView):
    # queryset = User.objects.all()
    # permission_classes =[IsAuthenticated]
    
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            return Response({
                'message': 'User created successfully',
                'user': {
                    'id': user.id,
                    'email': user.email,
                }
            }, status=HTTP_201_CREATED)
        
        return Response('not okey')
    
    def get(self,request):
        return HttpResponse('hello')



    