
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.status import *
from rest_framework.authentication import SessionAuthentication
from ...models import User,Profile
from rest_framework import permissions, viewsets
from .serializer import UserSerializer , ProfileSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.views import APIView, Response
from rest_framework.mixins import RetrieveModelMixin
from tinder_for_cats.user.api.v1 import serializer
from rest_framework import generics
from django.shortcuts import get_object_or_404



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



class ProfileUpdate(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'pk'

    def list(self, pk ,request, *args, **kwargs):
        queryset = Profile.objects.get(pk=pk)
        serializer = self.serializer_class(queryset,context={'request':request},many=True)
        return Response(serializer.data)

class AllProfile(APIView):
    def get(self,request):
        query = Profile.objects.all()
        serializer = ProfileSerializer(query , many=True,context={'request' : request})
        return Response(serializer.data)


@api_view(['GET'])
def Add_likes(request,pk):
    if request.method == 'GET':
        query = Profile.objects.get(pk=pk)
        serializer = ProfileSerializer(query)
        query.add_like()
        query.save()
        return Response(serializer.data['likes'])
    if request.method == 'POST':
        ...