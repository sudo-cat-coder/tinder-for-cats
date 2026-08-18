from ...models import User
from rest_framework import permissions, viewsets
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView, Response



# class UserViewSet(viewsets.ModelViewSet):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = [permissions.IsAuthenticated]
    
class UserAPiView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request,id=None):
        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            print(self.kwargs)
            return Response(serializer.data)
        user = User.objects.all()
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data)
        