from enum import unique
from operator import truediv

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import OneToOneField
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager
from django.db.models.signals import post_save , post_delete
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email address'),unique=True)
    username = None
    password = models.CharField(max_length=255, verbose_name='password')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# class User (abstractBaseUser):
#     email = models.EmailField(_('email address'),unique=True)
#     username = models.CharField(max_length=255 , unique=True)
#     password = models.CharField(max_length=255 , verbose_name='password')
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email


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
    avatar = models.ImageField(upload_to='avatar/' )
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255 , unique=True)
    bio = models.TextField(blank=True)
    gender = models.CharField(choices=GENDER , default=NONE)
    age = models.PositiveIntegerField()


    def __str__(self):
        return str(self.user_id.pk)



class UserPreference(models.Model):
    profile = OneToOneField(Profile)
    # fav_color = models.CharField(max_length=255)
    hobits = models.JSONField(default=dict)
    job = models.CharField(blank=True)
    city = models.CharField(blank=True)
    country = models.CharField(blank=True)

class Likes(models.Model):
    from_profile = models.ForeignKey(Profile)
    to_profile = models.ForeignKey(Profile)
    like = models.BooleanField(default=False)

    class Meta:
        unique_together = ('from_profile' , 'to_profile')



@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.get_or_create(user_id=instance)

# @receiver(post_delete, sender=User)
# def delete_profile(sender , instance , **kwargs):
#     Profile.objects.get(instance).delete()