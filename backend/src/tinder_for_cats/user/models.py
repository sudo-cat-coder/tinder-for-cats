from enum import unique
from operator import truediv

from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser ,PermissionsMixin
from django.db.models import OneToOneField
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver
from datetime import datetime

# Create your models here.
# class User(AbstractUser):
#     email = models.EmailField(_('email address'),unique=True)
#     username = None
#     password = models.CharField(max_length=255, verbose_name='password')

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

class User (AbstractBaseUser , PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    email = models.EmailField(_('email address'),unique=True)
    # username = models.CharField(max_length=255 , unique=True)
    password = models.CharField(max_length=255 , verbose_name='password')
    data_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):

    FEMALE = 'FEMALE'
    MALE = 'MALE'
    NONE = 'NONE'

    GENDER = [
    (FEMALE, "Female"),
    (MALE, "Male"),
    (NONE, "Prefer not to say"),
    ]

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/' ,blank=True,null=True)
    name = models.CharField(max_length=255 , null=True , blank=True )
    username = models.CharField( null=True , blank=True ,max_length=255 , unique=True)
    bio = models.TextField(blank=True)
    gender = models.CharField(choices=GENDER , default=NONE)
    age = models.PositiveIntegerField(default=1)
    likes = models.PositiveBigIntegerField(default=0)   # why i didn't use the like table? bcz my app is very simple 


    def __str__(self):
        return str(self.user)

    def add_like(self):
        self.likes += 1



class UserPreference(models.Model):
    profile = OneToOneField(Profile, on_delete=models.CASCADE)
    # fav_color = models.CharField(max_length=255)
    hobbies = models.JSONField(default=dict)
    job = models.CharField(blank=True)
    city = models.CharField(blank=True)
    country = models.CharField(blank=True)

# class Likes(models.Model):
#     from_profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
#     to_profile = models.ForeignKey(Profile)
#     like = models.BooleanField(default=False)

    # class Meta:
    #     unique_together = ('from_profile' , 'to_profile')



@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

# @receiver(post_delete, sender=User)
# def delete_profile(sender , instance , **kwargs):
#     Profile.objects.get(instance).delete()