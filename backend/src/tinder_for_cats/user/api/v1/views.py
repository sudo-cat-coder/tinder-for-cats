from rest_framework.status import HTTP_201_CREATED
from rest_framework.authentication import SessionAuthentication
from ...models import User
from rest_framework import permissions, viewsets
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView, Response

from tinder_for_cats.user.api.v1 import serializer



# class UserViewSet(viewsets.ModelViewSet):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [permissions.IsAuthenticated]
    
class UserAPiView(APIView):

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,id=None):
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            print(self.kwargs)
            return Response(serializer.data)
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        print(request.user)
        print(request.auth)
        return Response(serializer.data)


# class UserApiView(APIView):

#     def post(self,request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.password1 == serializer.password2 and serializer.is_valid():
#             serializer.save()
#             return Response(HTTP_201_CREATED)