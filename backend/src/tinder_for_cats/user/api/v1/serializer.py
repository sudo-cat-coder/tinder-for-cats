from dataclasses import field
from email.policy import default

from ...models import *
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','email' , 'password' , 'password1']
        extra_kwargs = {
            'password1': {
                'write_only': True
            }
        }

    def validate(self, data):
        if data['password'] != data['password1']:
            raise serializers.ValidationError('password dosnt match')
        return data

    def create(self, validated_data):

        validated_data.pop('password1')

        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )

        return user

    

class ProfileSerializer(serializers.ModelSerializer):

    likes = serializers.BigIntegerField(read_only=True)

    class Meta:
        model = Profile
        fields = ['user' ,'avatar' , 'name' , 'username' , 'bio' ,'gender' , 'age' , 'likes']

        def validate(self,data):
            ...

        def update(self,validated_data):
            ...