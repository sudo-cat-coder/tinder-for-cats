from ...models import *
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','email' , 'password']


